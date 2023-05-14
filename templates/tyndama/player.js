let currentMusic = 0;

const music = document.getElementById("#audio");

const album_img = document.querySelector('.album-image');
const song_title = document.querySelector('.player-title');
const artist = document.querySelector('.artist');
const curr_time = document.querySelector('.curr-time');
const duration = document.querySelector('.duration');
const  play_btn = document.querySelector('.btn-toggle-play');
const forward_btn = document.querySelector('.btn-next');
const previus_btn = document.querySelector('.btn-prev');

play_btn.addEventListener('click', () =>{
    play_btn.classList.toggle('pause')
})
