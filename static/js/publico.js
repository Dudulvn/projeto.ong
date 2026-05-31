document.addEventListener('DOMContentLoaded', function () {
    var botaoCopiar = document.getElementById('btn-copiar-pix');
    var chavePix = document.getElementById('chave-pix');
    var feedbackPix = document.getElementById('feedback-pix');

    if (botaoCopiar && chavePix) {
        botaoCopiar.addEventListener('click', function () {
            var texto = chavePix.textContent.trim();

            if (navigator.clipboard && navigator.clipboard.writeText) {
                navigator.clipboard.writeText(texto).then(function () {
                    mostrarFeedback('Chave Pix copiada!');
                }).catch(function () {
                    copiarManual(texto);
                });
            } else {
                copiarManual(texto);
            }
        });
    }

    function copiarManual(texto) {
        var area = document.createElement('textarea');
        area.value = texto;
        document.body.appendChild(area);
        area.select();
        try {
            document.execCommand('copy');
            mostrarFeedback('Chave Pix copiada!');
        } catch (e) {
            mostrarFeedback('Não foi possível copiar. Selecione e copie manualmente.');
        }
        document.body.removeChild(area);
    }

    function mostrarFeedback(mensagem) {
        if (!feedbackPix) {
            return;
        }
        feedbackPix.textContent = mensagem;
        setTimeout(function () {
            feedbackPix.textContent = '';
        }, 3000);
    }

    var linksAncora = document.querySelectorAll('.link-ancora');
    var menu = document.getElementById('menuPublico');

    linksAncora.forEach(function (link) {
        link.addEventListener('click', function () {
            if (menu && menu.classList.contains('show')) {
                var botao = document.querySelector('.navbar-toggler');
                if (botao) {
                    botao.click();
                }
            }
        });
    });
});
