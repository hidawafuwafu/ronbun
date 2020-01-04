var gulp = require('gulp');
var exec = require('gulp-exec');
var del = require('del');
var runSequence = require('run-sequence');

var texfile = 'main';
var filename = texfile + '.tex';
var indexfile = texfile + '.idx';
var pdffile = texfile + '.pdf';
 
gulp.task('latex',function() {
  return gulp.src('main.tex')
    .pipe( exec( 'simpdftex platex --mode dvipdfmx --maxpfb --extratexopts "-file-line-error" ' + filename ) );
});

gulp.task('index',function() {
  return gulp.src( indexfile )
    .pipe( exec( 'mendex -r -c -g -s dot.ist -p any ' + indexfile ) )
});

gulp.task('clean', function() {
	del( ['*.idx', '*.ind', '*.aux', '*.dvi', '*.ilg', '*.log', '*.toc', '*.synctex.gz' ] );
});

gulp.task('open', function() {
	return gulp.src( pdffile )
	  .pipe( exec( 'open ' + pdffile ) );
});

gulp.task('build', function() {
	runSequence(
	  'latex',
	  'index',
	  'latex',
	  'open'
	);
});
