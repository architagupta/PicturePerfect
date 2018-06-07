$("#view_file").click(function (e) {
   showUploadedImage()
});

$("#view_file").click(function (e) {
    showUploadedImage()
});


function showUploadedImage() {
    $.ajax({
        type: 'GET',
        cache: false,
        url: '/findImge',
        success: function (resp) {
            //alert(resp);
            //file_name = $('#images').context.URL.split('=')[1];
            if (resp != 'NULL')
                url = "../imagesfolder/" + resp;
            else
                url = "../static/images/upload_image.jpg"
            $('.column #imge').attr('src', url);
            //$('#formImg').removeAttr('hidden');
            $('#formImg').css({ display: 'block' });
        }
    });
}

function get_img() {
    src_img = "";
    $.ajax({
        type: 'GET',
        cache: false,
        url: '/filteredImge',
        success: function (data) {
            alert(data);
            src_img = data;
        }
    });
}

//$.getJSON($SCRIPT_ROOT + "_status",function (data) {
//        $('#Result').text(data);
//    }
//);

function getFilteredImage() {
    $.ajax({
        type: 'GET',
        cache: false,
        url: '/filtered',
        success: function (resp) {
            //alert(resp);
            //src_img = "";
            src_img = "";
            if (resp != null){
                $.ajax({
                    type: 'GET',
                    cache: false,
                    url: '/filteredImge',
                    success: function (data) {
                        //alert(data);
                        //src_img = data;
                        if (data != 'NULL')
                            url = "../thumbnails/" + data;
                        else
                            url = "../static/images/upload_image.jpg"
                        $('#mod_img').attr('src', url);
                        //$('#formImg').removeAttr('hidden');
                        $('#mod_img').css({ display: 'inline' });

                    }
                });
            }

            //a = get_img();
            //$.getJSON('/filteredImge',
            //    function (data) {
            //        alert("reached");
            //        src_img = data;
            //    });
            //src_img = "";
            //alert(src_img);
            //if (resp != 'NULL')
            //    url = "../imagesfolder/" + resp;
            //else
            //    url = "../static/images/upload_image.jpg"
            //$('.column #mod_img').attr('src', url);
            ////$('#formImg').removeAttr('hidden');
            //$('#mod_img').css({ display: 'block' });
        }
    });
}
