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

if __name__ == '__main__':
    app.run(debug=True)
