window.addEventListener('load', () => {
    page = new Page([ "#classes", "#new2", "#new3", "#new4", "#new5", "#new6"]);
    page.change('#classes');

    let a = document.querySelector('#next_button');
    console.log(a);

    document.querySelector('#next_button').addEventListener('click', () => { page.next(); });
    document.querySelector('#prev_button').addEventListener('click', () => { page.prev(); });
    (function () {
        var recognition;
        var nowRecognition = false;
        var $finalSpan = document.querySelector('#final_span');
        var $interimSpan = document.querySelector('#interim_span');
        function start() {
            recognition = new webkitSpeechRecognition();
            recognition.lang = document.querySelector('#select2').value;
            recognition.continuous = true;
            recognition.interimResults = false;
            recognition.onresult = function (e) {
                console.log( "seramic.js:21" + '[onresult]', e.results.length);
                var finalText = '';
                var interimText = '';
                console.log( e.results[e.results.length-1][0].transcript);
                interimText = e.results[e.results.length-1][0].transcript;
                $interimSpan.textContent = interimText;
                console.log(" seramic.js:33  " + interimText );
                if (interimText === "次へ") page.next();
                else if (interimText === "戻る") page.prev();
                $finalSpan.textContent = finalText;
            };
            recognition.onstart = function () {
                console.debug('[onstart]');
            };
            recognition.onaudiostart = function () {
                console.debug('[onaudiostart]');
            }
            recognition.onsoundstart = function () {
                console.debug('[onsoundstart]');
            }
            recognition.onspeechstart = function () {
                console.debug('[onspeechstart]');
            }
            recognition.onspeechend = function () {
                console.debug('[onspeechend]');
            }
            recognition.onsoundend = function () {
                console.debug('[onsoundend]');
            }
            recognition.onaudioend = function () {
                console.debug('[audioend]');
            }
            recognition.onnomatch = function () {
                console.debug('[onnomatch]');
            }
            recognition.onerror = function () {
                console.debug('[onerror]');
            }
            recognition.onstart = function () {
                console.debug('[onstart]');
            }
            recognition.onend = function () {
                console.debug('[onend]');
            }
            recognition.start();
            nowRecognition = true;
        };
        function stop() {
            recognition.stop();
            nowRecognition = false;
        }


        document.querySelector('#btn2').onclick = function () {

            // unsupported.
            if (!'webkitSpeechRecognition' in window) {
                alert('Web Speech API には未対応です.');
                return;
            }

            if (nowRecognition) {
                stop();
                this.value = '音声認識を継続的に行う';
                this.className = '';
            } else {
                start();
                console.log("seramic.js:94 start");
                this.value = '音声認識を止める';
                this.className = 'select';
            }
        }
    })();
});
