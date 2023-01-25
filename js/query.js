jQuery.ajax({
    url: 'http://127.0.0.1:5000',
    type: 'GET',
    success: function (data) {
        JSON.stringify(data)
        $("#precio1").html(data[0][2]);
        $("#disp1").html(data[0][3]);

        $("#precio2").html(data[1][2]);
        $("#disp2").html(data[1][3]);

        $("#precio3").html(data[2][2]);
        $("#disp3").html(data[2][3]);

        $("#precio4").html(data[3][2]);
        $("#disp4").html(data[3][3]);

        $("#precio5").html(data[4][2]);
        $("#disp5").html(data[4][3]);

        $("#precio6").html(data[5][2]);
        $("#disp6").html(data[5][3]);

        $("#precio7").html(data[6][2]);
        $("#disp7").html(data[6][3]);

        $("#precio8").html(data[7][2]);
        $("#disp8").html(data[7][3]);

        $("#precio9").html(data[8][2]);
        $("#disp9").html(data[8][3]);

        $("#precio10").html(data[9][2]);
        $("#disp10").html(data[9][3]);

        $("#precio11").html(data[10][2]);
        $("#disp11").html(data[10][3]);

        $("#precio12").html(data[11][2]);
        $("#disp12").html(data[11][3]);
    }
}); 