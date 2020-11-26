$(document).ready(main)
var clickeado = true;
var guardado =true;
var islogin=true;
function main() {
    //funcion que oculta y muestra el menu en el modo responsive
    $(function() {
        $('#menu_bar').click(
            function() {
                if (clickeado) {
                    $('.bt_menu').css("color", '#ffa11e');
                    //  $('.menu').show();
                    $('.menu').animate({
                        right: "0"
                    });
                    clickeado = false;

                } else {
                    $('.bt_menu').css("color", 'white');
                    // $('.menu').hide();
                    $('.menu').animate({
                        right: "100%"
                    });
                    clickeado = true;
                }
            });
    });
    //funcion que detecta cuando la ventana/pagina cambia de tamaño y cambia el desplazamiento del nav
    $(function() {
        $(window).resize(
            function() {
                // si la pantalla llega al ancho de escritorio 
                // el menu nav aparece en una fila
                if ($(window).width() > 818) {
                    //  $('.menu').show();
                    $('.menu').css("right", "");
                    // en caso que se menor al ancho 
                    // se oculta el nav
                } else if ($(window).width() <= 818) {
                    $('.menu').css("right", "100%");
                    //  $('.menu').hide();
                }
            });
    });
    // menulateral
    $(function(){
        $('.login').click(
            function(){
                if (islogin) {
                    $('.opc-user').show();
                    islogin=false;
                }else{
                    $('.opc-user').hide()
                    islogin=true;
                }
            });

    });
    //mensaje de redes sociales
    $(function() {
        $(".icon-whatsapp,.icon-instagram,.icon-facebook2").click(function() {
            alert("Próximamente estarán disponibles las redes sociales..No te lo pierdas!!")
        });
    });
    // Funcion para ir hacia arriba de la pagina cuando el scroll Vertical llega hasta el fin de contenido
    $(function() {
        $(".subir-inicio").click(
            function() {
                $("body,html").animate({
                    scrollTop: "0px"
                }, 1500);
            }
        );
    });
    $(function() {
        $(".icon-whatsapp,.icon-instagram,.icon-facebook2").click(function() {
            alert("Próximamente estarán disponibles las redes sociales..No te lo pierdas!!")
        });
    });
  
    $(function() {
        $("#formulario").validate({
            rules: {
                nombre: {
                    required: true,
                    minlength: 3,
                    maxlength: 15
                },
                pais: {
                    minlength: 3,
                    maxlength: 15
                },
                correo: {
                    required: true,
                    email: true
                },
                asunto: {
                    required: true,
                    minlength: 4,
                    maxlength: 15
                },
                comentario: {
                    required: true,
                    minlength: 10,
                    maxlength: 100
                },


            },
            messages: {
                nombre: {
                    required: 'Porfavor ingrese su nombre',
                    minlength: 'Largo insuficiente',
                    maxlength: 'Maximo 15 caracteres'
                },
                pais: {
                    minlength: 'Ingrese al menos 3 caracteres',
                    maxlength: 'Maximo 15 caracteres'
                },
                correo: {
                    required: 'Porfavor ingrese su correo',
                    email: 'Ingrese un email valido'


                },
                asunto: {
                    required: 'Ingrese el motivo de su comentario',
                    minlength: 'Largo insuficiente',
                    maxlength: 'Largo excedido'
                },
                comentario: {
                    required: 'Ingrese su comentario porfavor',
                    minlength: 'Comentario muy corto',
                    maxlength: 'Largo excedido'
                },
            },
            errorElement: "div"
        });
    });
    function Eliminar(id){
        Swal.fire({
            title: '¿Seguro de eliminar este item?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Si,confirmo eliminacion',
            cancelButtonText:'Camceñar'
          }).then((result) => {
            if (result.isConfirmed) {
              Swal.fire(
                window.location.href='Peliserie/'+id+'/edit/'
              )
            }
          })
    }

};