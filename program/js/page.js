class Page {
  constructor( pages ) {
    this.pages = pages;/*ここで移動する変数の宣言*/
    this.now = pages[0];
    this.page_size = pages.length;
    console.log( this.page_size );
  }
  change( page ) {
    let pages1 = document.querySelectorAll('.page');　/*クラスを指定する　（.pageはクラス名） */
    for( let p of pages1 ) {　
      p.style.display = "none";
    }
    console.log( page );
    document.querySelector( page ).style.display = "block";
    this.now = page;
  }
  next() {
    let number = this.pages.indexOf( this.now );
    console.log( number, this.page_size );
    if( number < this.page_size-1 ) {
      let a = document.querySelector( this.now );//.style.display = "none";
      console.log(this.now,a);
      this.change( this.pages[number+1]);
    }
  }
  prev() {
    let number = this.pages.indexOf( this.now );
    console.log( number, this.page_size );
    if( 0 < number ) {
      let a = document.querySelector( this.now );//.style.display = "none";
      console.log(this.now,a);
      this.change( this.pages[number-1]);
    }
  }
}

// /*change を宣言　＝＞　ボタンなどを押された後の処理 */
// const change = ( page ) => {　/*アロー関数 */
//   let pages1 = document.querySelectorAll('.page');　/*クラスを指定する　（.pageはクラス名） */
//   for( p of pages1 ) {　
//     p.style.display = "none";
//   }
//   console.log( page );
//   document.querySelector( page ).style.display = "block";
// }

// /* ボタンを押されたときの処理*/
// window.addEventListener('load',() => {
//   change( "#classes" );
//   let nl = new nylon();
//   document.querySelector('#new_btn').addEventListener('click', () => {
//     nl.emit( "page", {page: '#new2'});
//   });

//   let nl2 = new nylon();
//   nl2.on ('page', (key, value) => {
//     change( value.page );
//   });
// })
// /* ここを分岐させたいな なんで分岐できたの？*/
// /* 2から3へ*/
// window.addEventListener('load',() => {
//   change( "#classes" );
//   let nl = new nylon();
//   document.querySelector('#new_btn2').addEventListener('click', () => {
//     nl.emit( "page", {page: '#new3'});
//   });

//   let nl2 = new nylon();
//   nl2.on ('page', (key, value) => {
//     change( value.page );
//   });
// })

// /* 3から4へ*/
// window.addEventListener('load',() => {
//   change( "#classes" );
//   let nl = new nylon();
//   document.querySelector('#new_btn3').addEventListener('click', () => {
//     nl.emit( "page", {page: '#new4'});
//   });

//   let nl2 = new nylon();
//   nl2.on ('page', (key, value) => {
//     change( value.page );
//   });
// })
// /* 2から1へ*/
// window.addEventListener('load',() => {
//   change( "#classes" );
//   let nl = new nylon();
//   document.querySelector('#new_btn0').addEventListener('click', () => {
//     nl.emit( "page", {page: '#classes'});
//   });

//   let nl2 = new nylon();
//   nl2.on ('page', (key, value) => {
//     change( value.page );
//   });
// })
// /* 3から2へ*/
// window.addEventListener('load',() => {
//   change( "#classes" );
//   let nl = new nylon();
//   document.querySelector('#new_btn4').addEventListener('click', () => {
//     nl.emit( "page", {page: '#new2'});
//   });

//   let nl2 = new nylon();
//   nl2.on ('page', (key, value) => {
//     change( value.page );
//   });
// })
// /* 4から3へ*/
// window.addEventListener('load',() => {
//   change( "#classes" );
//   let nl = new nylon();
//   document.querySelector('#new_btn5').addEventListener('click', () => {
//     nl.emit( "page", {page: '#new3'});
//   });

//   let nl2 = new nylon();
//   nl2.on ('page', (key, value) => {
//     change( value.page );
//   });
// })
// /* 4から5へ*/
// window.addEventListener('load',() => {
//   change( "#classes" );
//   let nl = new nylon();
//   document.querySelector('#new_btn6').addEventListener('click', () => {
//     nl.emit( "page", {page: '#new5'});
//   });

//   let nl2 = new nylon();
//   nl2.on ('page', (key, value) => {
//     change( value.page );
//   });
// })
// /* 5から6へ*/
// window.addEventListener('load',() => {
//   change( "#classes" );
//   let nl = new nylon();
//   document.querySelector('#new_btn8').addEventListener('click', () => {
//     nl.emit( "page", {page: '#new6'});
//   });

//   let nl2 = new nylon();
//   nl2.on ('page', (key, value) => {
//     change( value.page );
//   });
// })
// /* 5から6へ*/
// window.addEventListener('load',() => {
//   change( "#classes" );
//   let nl = new nylon();
//   document.querySelector('#new_btn9').addEventListener('click', () => {
//     nl.emit( "page", {page: '#new5'});
//   });

//   let nl2 = new nylon();
//   nl2.on ('page', (key, value) => {
//     change( value.page );
//   });
// })
// /* 5から4へ*/
// window.addEventListener('load',() => {
//   change( "#classes" );
//   let nl = new nylon();
//   document.querySelector('#new_btn7').addEventListener('click', () => {
//     nl.emit( "page", {page: '#new4'});
//   });

//   let nl2 = new nylon();
//   nl2.on ('page', (key, value) => {
//     change( value.page );
//   });
// })
// /* 6から1へ*/
// window.addEventListener('load',() => {
//   change( "#classes" );
//   let nl = new nylon();
//   document.querySelector('#new_btn10').addEventListener('click', () => {
//     nl.emit( "page", {page: '#classes'});
//   });

//   let nl2 = new nylon();
//   nl2.on ('page', (key, value) => {
//     change( value.page );
//   });
// })
