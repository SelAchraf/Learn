let container = document.createElement('div');
document.body.appendChild(container);
container.style.textAlign = 'center';

let name = ['achraf','mouiz', 'ranim', 'said', 'hadjer'];
let ages = ['20 years old', '14 years old', '17 years old', '55 years old', '50 years old'];

function element(name, ages){
    let card = document.createElement('div');
    let title = document.createElement('h2');
    let age = document.createElement('p');
    let img = document.createElement('img');

    let title_content = document.createTextNode(name);
    let age_content = document.createTextNode(ages);
    
    title.appendChild(title_content);
    age.appendChild(age_content);
    img.src = 'TLauncher.png';

    card.style.width = '200px';
    card .style.height = '300px';
    card.style.margin = '10px';
    card.style.backgroundColor = '#444';
    card.style.padding = '10px';
    card.style.display = 'inline-block';
    img.style.width = '100%';
    img.style.height = '65%';

    
    card.appendChild(title);
    card.appendChild(age);
    card.appendChild(img);
    container.appendChild(card);
}

for (let i = 0; i<5; i++){
    element(name[i], ages[i]);
}