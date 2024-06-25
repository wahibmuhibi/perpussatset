from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# URL dari file CSV
url = "https://siplah.kemdikbud.go.id/sds/lookup-tables/msts/books/non_text_books.csv"

# Baca CSV dari URL ke DataFrame
df = pd.read_csv(url)

# Fungsi untuk mendapatkan data buku berdasarkan halaman
def get_books(page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    return df.iloc[start:end]

# Fungsi untuk menghitung jumlah buku
def count_books():
    return df.shape[0]

# Fungsi untuk mendapatkan variasi harga dari prices
def get_price_variety():
    prices = df['prices'].dropna().tolist()
    price_count = {
        '0-20000': 0,
        '20001-40000': 0,
        '40001-60000': 0,
        '60001-80000': 0,
        '80001-100000': 0,
        'Above 100000': 0  # Kategori baru untuk harga di atas 100000
    }
    
    for price_list in prices:
        for price_dict in eval(price_list):
            price = price_dict['price']
            if price <= 20000:
                price_count['0-20000'] += 1
            elif price <= 40000:
                price_count['20001-40000'] += 1
            elif price <= 60000:
                price_count['40001-60000'] += 1
            elif price <= 80000:
                price_count['60001-80000'] += 1
            elif price <= 100000:
                price_count['80001-100000'] += 1
            else:
                price_count['Above 100000'] += 1
    
    return price_count

# Route untuk halaman utama dengan pagination
@app.route('/')
def index():
    # Ambil nomor halaman dari query string, defaultnya 1
    page = int(request.args.get('page', 1))
    per_page = 9  # Jumlah buku per halaman
    total_books = df.shape[0]
    total_pages = total_books // per_page + (1 if total_books % per_page > 0 else 0)

    books = get_books(page, per_page)
    return render_template('index.html', books=books.to_dict(orient='records'), page=page, total_pages=total_pages)

# Route untuk halaman detail buku
@app.route('/detail/<id>')
def detail(id):
    book = df[df['id'] == id].iloc[0].to_dict()
    return render_template('detail.html', book=book)

# Route untuk hasil pencarian
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query:
        # Lakukan pencarian berdasarkan 'title' atau 'author'
        results = df[df['title'].str.contains(query, case=False) | df['author'].str.contains(query, case=False)]
    else:
        results = df
    return render_template('search_results.html', books=results.to_dict(orient='records'), query=query)

# Route untuk halaman dashboard
@app.route('/dashboard')
def dashboard():
    total_books = count_books()
    price_variety = get_price_variety()
    return render_template('dashboard.html', total_books=total_books, price_variety_json=price_variety)

if __name__ == '__main__':
    app.run(debug=True)
