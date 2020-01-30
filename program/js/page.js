class Page {
  constructor( pages ) {
    this.pages = pages;
      console.log(" this.pages  " + this.pages );
    this.now = pages[0];
      console.log(" this.now  " + this.now );
    this.page_size = pages.length;
      console.log(" this.page_size  " + this.page_size );
  }
  change( page ) {
    let pages1 = document.querySelectorAll('.page');
    console.log(" pages1  " + pages1 );
    for( let p of pages1 ) {　
      p.style.display = "none";
    }
    document.querySelector( page ).style.display = "block";
    this.now = page;
    console.log(" this.now  " + this.now );
  }
  next() {
    let number = this.pages.indexOf( this.now );
    console.log(" number  " + number );
    if( number < this.page_size-1 ) {
      let a = document.querySelector( this.now );
    console.log(" this.pages[number+1]  " + this.pages[number+1] );
      this.change( this.pages[number+1]);
    }
  }
  prev() {
    let number = this.pages.indexOf( this.now );
    if( 0 < number ) {
      let a = document.querySelector( this.now );
      this.change( this.pages[number-1]);
    }
  }
}
