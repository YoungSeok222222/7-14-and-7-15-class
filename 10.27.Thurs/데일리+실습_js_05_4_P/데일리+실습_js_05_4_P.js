/* 
  아래에 코드를 작성해주세요.
*/
  

const musicSearchUrl = 'http://ws.audioscrobbler.com/2.0/?method=album.search&album=believe&api_key=b9416ee6b353c5977e433ca1ccfcad23&format=json'

const keyWord = document.querySelector('.search-box__input')
const searchBtn = document.querySelector('.search-box_-button')
console.log(keyWord)

const fetchAlbums = function(keyWord){
  axios({
    method :'GET',
    url : musicSearchUrl,
  })
  .then((keyWord) => {
    console.log(keyWord)

  })

}

searchBtn.addEventListener('click',fetchAlbums)


