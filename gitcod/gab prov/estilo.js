document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;

    alert(`Obrigado por entrar em contato, ${name}! Nós responderemos para ${email}.`);
});