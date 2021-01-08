# CS336-multimedia-information-retrieval
<!DOCTYPE html>
<html lang="en">
<head>
    <title>FINAL MACHINE LEARNING PROJECT</title>
    <meta charset="utf-8">
    <!--meta name="viewport" content="width=device-width, initial-scale=1"-->
    <link rel="icon" type="image/png" href="https://nguyenvanhieu.vn/wp-content/uploads/2018/08/pointer.png">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script>
        function clear_result() {
            $('.result').text('')
            $('textarea').text('')
        }
    </script>
</head>
<body>

<div class="container">
    <h2>CLASSIFY TOPIC OF TITLE</h2>
    <p>Classify topic of title from title</p>
    <form method="post">
        <div class="form-group">
            <label for="title_result">Just paste your title here:</label>
            <textarea class="form-control" rows="5" name="title_result" id="title_result">{{title_result}}</textarea>
            <input type="submit" value="Submit" class="btn btn-success btn-lg" style="margin-top: 20px;">
            <input type="reset" value="Reset" class="btn btn-default btn-lg" style="margin-top: 20px;"
                   onclick="clear_result()">
        </div>
    </form>
    <div class="result">
        <h4>Predict result:</h4>
        {% if class_title %}
        <p>Title topic: <strong>{{ class_title }}</strong></p>
        {% endif %}
    </div>
</div>
<div class="container" style="margin-top:20px;">
    <p>List of title topic:</p>
    <pre>Thể thao        Giáo dục        Công nghệ        Chính trị        Pháp luật        Kinh doanh</pre>
    <p>Made with <span style="color: red;">❤</span> by <a href="https://nguyenvanhieu.vn">Nguyễn Văn Hiếu</a>.</p>
    <p>Edited with <span style="color: red;">❤</span> by <a href="https://www.facebook.com/profile.php?id=100027617961231">Thái Hoàng Nhân</a>.</a></p>
    <p>Reference from <a href="https://github.com/NguyenVanHieuBlog/programing-language-identify">NguyenVanHieuBlog/programing-language-identify</a>.</p>
</div>
</body>
</html>
