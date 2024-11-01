let photos = document.querySelectorAll('.onclick_photos')
let main_photo = document.querySelector('#main_photo')

photos.forEach(
    photo => {
        photo.onclick = function(){
            main_photo.src = this.src;
        }
    }
)