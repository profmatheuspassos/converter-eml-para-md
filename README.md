# Conversor de E-mails EML para Markdown

Este script Python foi desenvolvido para facilitar a conversão de arquivos de e-mails salvos no formato `.eml` (utilizado por clientes de e-mail como o Microsoft Outlook) para o formato Markdown (`.md`). Este processo permite uma melhor integração e manipulação dos conteúdos dos e-mails em plataformas que suportam Markdown, como sistemas de gestão de conhecimento (Obsidian) ou páginas estáticas geradas via Jekyll, Hugo, entre outros.

## Funcionalidades

- **Conversão Automática**: O script busca por todos os arquivos `.eml` em uma pasta especificada, converte cada um em um arquivo Markdown e salva na pasta de destino designada.
- **Preservação de Metadados**: Cada arquivo Markdown gerado começa com a data e hora original do envio do e-mail, formatados como `YYYY-MM-DD - HH:MM`, fornecendo um contexto temporal para o conteúdo do e-mail.
- **Feedback ao Usuário e Logging**: Caso não existam arquivos `.eml` na pasta de origem, o script informa ao usuário que nenhum arquivo foi encontrado, evitando confusões ou execuções desnecessárias. Logs detalhados ajudam na depuração e acompanhamento da execução.

## Como Usar

### Pré-Requisitos

Antes de executar o script, certifique-se de que você possui Python instalado em seu sistema e que as bibliotecas `email`, `markdownify` e `logging` estão instaladas. Você pode instalar qualquer dependência ausente utilizando o `pip`:

```bash
pip install markdownify
```

### Execução

1. Clone o repositório ou baixe o script para o seu sistema.
2. Modifique as variáveis `caminhoPastaFonte` e `pastaDestino` no script para refletir os caminhos desejados em seu ambiente.
3. Execute o script com o seguinte comando no terminal:

```bash
python conversor-eml-para-md.py
```

### Log de Atividades

O script inclui um sistema de log básico configurado para registrar informações essenciais durante a execução. Os logs incluem erros, avisos e mensagens informativas que ajudam a acompanhar o progresso e identificar potenciais problemas. Os logs são exibidos no console durante a execução e podem ser redirecionados para um arquivo, se necessário, ajustando as configurações de logging no início do script.

### Configuração

Você pode configurar o script para diferentes pastas de origem e destino modificando as variáveis no bloco de exemplo de uso do script.

## Contribuições

Contribuições são bem-vindas! Se você deseja melhorar o script, sinta-se à vontade para forkar o repositório, fazer suas alterações e abrir um pull request. Estamos particularmente interessados em melhorar a conversão de formatos, a eficiência do script e em adicionar suporte para diferentes clientes de e-mail.

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.