$(document).ready(function () {
    // Init
    $('.image-section-ResNet50').hide();
    $('.loaderResNet50').hide();
    $('#resultResNet50').hide();
    $('#play').show();
   
    // Upload Preview
    function readURLResNet50(input) {
        

        if (input.files && input.files[0]) {
            var reader = new FileReader();
           
            reader.onload = function (e) {
		
		 console.log("url-data",e.target.result);
		console.log("input",input.files);
		console.log("input",input.files[0].name);
		var audiofilename=input.files[0].name;
		
		console.log("audiofilename",audiofilename);
		
		var audioname=document.getElementById("imageUploadResNet50").value;
                console.log("audioname",audioname);
                $('#imagePreviewResNet50').css('background-image', 'url(' + e.target.result + ')');
		
                $('#imagePreviewResNet50').hide();
                $('#imagePreviewResNet50').fadeIn(650);
 
            }
            reader.readAsDataURL(input.files[0]);
        }
    }


    $("#imageUploadResNet50").change(function () {
        $('.image-section-ResNet50').show();
        $('#play').show();
       
        $('#btn-predict-ResNet50').show();

        $('#resultResNet50').text('');
        $('#resultResNet50').show();
	
        readURLResNet50(this);
    });


    // Predict
    $('#btn-predict-ResNet50').click(function () {
        var form_data = new FormData($('#upload-file-ResNet50')[0]);
        //form_Data.append('audio', audioBlob, 'audio.wav')
        // Show loading animation
        $(this).hide();
        $('.loaderResNet50').show();

        // Make prediction by calling api /predictResNet50

        $.ajax({
            type: 'POST',
            url: '/predictResNet50',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.loaderResNet50').hide();
                $('#resultResNet50').fadeIn(600);
                $('#resultResNet50').text(' Result:  ' + data);
                console.log('ResNet50 Success!');
            },
        });
    });

});