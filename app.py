from flask import Flask, render_template, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    if not url:
        return jsonify({"error": "Jani link to dalo!"})

    # HD Quality aur Fast Response ke liye Options
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'quiet': True,
        'no_warnings': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info.get('url', None)
            title = info.get('title', 'Nawab_Zada_HD_Video')
            thumbnail = info.get('thumbnail', '')
            
            return jsonify({
                "title": title,
                "download_link": video_url,
                "thumbnail": thumbnail
            })
    except Exception as e:
        return jsonify({"error": "Link invalid hai ya video private hai!"})

if __name__ == '__main__':
    app.run(debug=True)
