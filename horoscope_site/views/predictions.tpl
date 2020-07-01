<html>
    <head>
        <meta charset='utf-8'>
        <title>Гороскоп на сегодня</title>
        <link
        rel="stylesheet"
        href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css
        "
        integrity="sha384-
        MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"
        crossorigin="anonymous"
        />
        <script src="http://code.jquery.com/jquery-3.3.1.min.js"></script>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@600&display=swap');

            h1, h2 {
                font-family: 'Source Sans Pro', sans-serif;
                color: white;
                text-align: center;
            }

            .content {
                width: 20 rem;
                font-family: 'Oswald', sans-serif;
                color: white;
            }
        </style>
    </head>

    <body style="background: #5F9EA0;">
        <div class="container">
            <h1><span id="forecasts">Что день</span> {{ date }} готовит</h1>
            % if special_date:
                <h2>Сегодня супер особенный день!</h2>
            % end
            <div class="row">
                % for index, pred in enumerate(predictions):
                    <div class="col-4 mt-2 content" id="pred-{{ index }}">
                        {{ pred }}
                    </div>
                % end
                <div class="col-4 mt-2 content" id="pred-5"></div>
            </div>
        </div>
    </body>
    <script language="javascript">
        forecast_url = "http://localhost:8080/api/forecasts";

        function set_content_in_divs(paragraphs) {
            $.each(paragraphs, function(index, value) {
                p = $("#pred-" + index);
                p.html("<p>" + value + "</p>");
                console.log(index);
                console.log(value);
            });
        }

        $('#forecasts').click(function() {
            $.getJSON(forecast_url, function(data) {
                predictions = data["predictions"];
                set_content_in_divs(predictions);
            });
        });
    </script>
</html>
