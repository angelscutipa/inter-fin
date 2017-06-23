$(document).ready(function(){
	formSubmit()
})
function formSubmit(){
	$('#contenido').submit(function(e){
		e.preventDefault()
		var correo=$('.correo').val()
		var password=$('.password').val()
		var consulta=$('.consulta').val()

		var data='correo='+correo+'&password='+password+'&consulta='+consulta;

		$.ajax({
			url:'interesado.py',
			type: 'get',
			data: data,
			beforeSend: function () {
                    $("#contenido .msn").html("Procesando, espere por favor...");
            },
            success:  function (response) {
					$("#contenido .msn").html("");
                    $("#contenido .show").html(response);
            }
		})

	})
}