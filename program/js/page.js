class Page {
  constructor( pages ) {
    this.pages = pages;
    this.now = pages[0];
    this.page_size = pages.length;
  }
  change( page ) {
    let pages1 = document.querySelectorAll('.page');
    for( let p of pages1 ) {　
      p.style.display = "none";
    }
    document.querySelector( page ).style.display = "block";
    this.now = page;
  }
  next() {
    let number = this.pages.indexOf( this.now );
    if( number < this.page_size-1 ) {
      let a = document.querySelector( this.now );
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
