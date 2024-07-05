<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST["nome"];
    $data = date('d/m/Y');  // Pode usar a data do formulário se preferir

    // Carregar o modelo existente
    $modeloPath = "caminho/do/seu/modelo.docx";
    $doc = file_get_contents($modeloPath);

    // Substituir marcadores no documento
    $doc = str_replace("{NOME}", $nome, $doc);
    $doc = str_replace("{DATA}", $data, $doc);

    // Salvar o novo documento
    $novoPath = "caminho/do/seu/novo_documento.docx";
    file_put_contents($novoPath, $doc);
}
?>
