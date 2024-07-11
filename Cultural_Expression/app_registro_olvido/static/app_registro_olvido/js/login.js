
(() => {
    'use strict';
    //General el ID  --este es el que permite general el id de nuetsros usuarios registrados . ciltural expression 
    let count = 1; // Iniciar el contador para el usuario en cultural expression 
    function generarID() {
        let id = "log" + count; // Construir el ID con el contador actual
        count++; 
        return id; // Retornar el ID generado
    }

    // Obtener el botón de "Registrar"
    const botonRegistrar = document.getElementById('btn_ingresar');

    // Agregar evento de clic al botón de "Registrar"
    botonRegistrar.addEventListener('click', event => {
        event.preventDefault();
        // Obtener el formulario asociado al botón de "Registrar"
        const formulario = botonRegistrar.closest('form');

        // Verificar la validez de cada campo
        let aliasValido = formulario.querySelector('#Aliasinput').value.trim() !== '';
        let contraseñaValida = formulario.querySelector('#Contraseñainput').value.trim() !== '';
        let termValido = formulario.querySelector('#checkTerms').checked;


        // Agregar clase de validación al formulario
        formulario.classList.add('was-validated');

        const id = generarID();

        console.log("ID generado:", id); // Mostrar el ID en la consola
        // Mostrar mensaje de éxito
        Swal.fire({
            title: "Éxito",
            text: "Registro exitoso",
            icon: "success",
            button: "OK",
            customClass: {
                popup: 'custom-modal',
            }
        });

        

        formulario.reset();
        inputs.forEach(input => {
            input.classList.remove('is-invalid');
        });
        formulario.classList.remove('was-validated');
    });
})();



//validar por caracteres especiales 
const formulario = document.getElementById('formulario');

const inputs= document.querySelectorAll('#formulario input')

const expresiones={
    alias: /^[a-zA-Z8-9\_\-]{8,16}$/,
    contraseña: /^.{8,16}$/
}

const campos = {
    alias: false,
    contraseña : false
}

const validarFormulario = (e)=>{
    switch (e.target.name){
        case 'alias':
            validarCampo(expresiones.alias, e.target, 'alias')
        
            break
        case 'contraseña':
            validarCampo(expresiones.contraseña, e.target, 'contraseña')
            break
            
    }
}

//funcion para tdoos los campos
const validarCampo = (expresion , input , campo) => {
    if(expresion.test(input.value)){
        document.querySelector(`#grupo_${campo} .error`).classList.remove('error-activo');
        campos[campo] = true;
    } else{
        document.querySelector(`#grupo_${campo} .error`).classList.add('error-activo');
        campos[campo] = false;

    }
}

inputs.forEach((input)=>{
    input.addEventListener('keyup' ,validarFormulario);
    input.addEventListener('blur' ,validarFormulario);
})

formulario.addEventListener('submit', (e) => {
    e.preventDefault();

    if( campos.alias && campos.contraseña){
        formulario.reset();

    }
});




//id


let count = 1;

function generarID() {
    let id = "log" + count; 
    count++; 
    return id; 
}

// Ejemplo de uso:
console.log(generarID()); // Output: use1

/*const formulario = document.getElementById('formulario');

const inputs= document.querySelectorAll('#formulario input')

const expresiones={
    alias: /^[a-zA-Z8-9\_\-]{8,16}$/,
    contraseña: /^.{8,16}$/
}

const campos = {
    alias: false,
    contraseña : false
}

const validarFormulario = (e)=>{
    switch (e.target.name){
        case 'alias':
            validarCampo(expresiones.alias, e.target, 'alias')
        
            break
        case 'contraseña':
            validarCampo(expresiones.contraseña, e.target, 'contraseña')
            break
            
    }
}

//funcion para tdoos los campos
const validarCampo = (expresion , input , campo) => {
    if(expresion.test(input.value)){
        document.querySelector(`#grupo_${campo} .error`).classList.remove('error-activo');
        campos[campo] = true;
    } else{
        document.querySelector(`#grupo_${campo} .error`).classList.add('error-activo');
        campos[campo] = false;

    }
}

inputs.forEach((input)=>{
    input.addEventListener('keyup' ,validarFormulario);
    input.addEventListener('blur' ,validarFormulario);
})

formulario.addEventListener('submit', (e) => {
    e.preventDefault();

    if( campos.alias && campos.contraseña){
        formulario.reset();
    }
});



//contraseña




const validarcontraseña = () => {
    const inputcontraseña1 = document.getElementById ('contraseñainput')
    const inputcontraseña2 = document.getElementById ('contraseñainput2')

    if (inputcontraseña1.value !== inputcontraseña2){

    }
}*/