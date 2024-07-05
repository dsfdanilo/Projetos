const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const Docxtemplater = require('docxtemplater');
const JSZip = require('jszip');
const { promisify } = require('util');

const app = express();
const port = 3000;

app.use(bodyParser.json());

app.post('/editarDocumento', async (req, res) => {
    const { nome } = req.body;

    try {
        // Ler o conteúdo do modelo do documento
        const content = fs.readFileSync('modelo.docx', 'binary');
        const zip = new JSZip(content);
        const doc = new Docxtemplater().loadZip(zip);

        // Preencher os campos no documento
        doc.setData({ NOME: nome, SUA_EMPRESA: 'Sua Empresa' });
        doc.render();

        // Gerar o documento editado
        const editedContent = doc.getZip().generate({ type: 'nodebuffer' });

        // Salvar o documento editado (opcional)
        fs.writeFileSync('documento_editado.docx', editedContent);

        res.setHeader('Content-Type', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document');
        res.send(editedContent);
    } catch (error) {
        console.error('Erro:', error);
        res.status(500).send('Erro ao editar o documento.');
    }
});

app.use(express.static('public'));

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});
