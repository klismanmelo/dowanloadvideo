# 🎬 Baixador de Vídeos do YouTube com Streamlit

Este projeto é uma aplicação simples que utiliza Python, Streamlit e a biblioteca pytube para baixar vídeos do YouTube de maneira fácil e intuitiva. Ao inserir a URL do vídeo, o usuário pode visualizar informações sobre o vídeo e fazer o download diretamente para seu computador.

## Funcionalidades

- **Visualização de Título e Visualizações**: Exibe o título e o número de visualizações do vídeo do YouTube.
- **Download de Vídeo**: Baixa o vídeo em sua melhor qualidade disponível diretamente para a pasta `downloads`.
- **Interface Interativa**: A interface é desenvolvida com Streamlit, tornando a interação simples e rápida.

## Tecnologias Usadas

- **Python**: Linguagem de programação usada para o backend.
- **Streamlit**: Framework para criação de aplicações web interativas.
- **pytube**: Biblioteca para baixar vídeos do YouTube.
- **os**: Biblioteca para manipulação do sistema de arquivos.
- **sys**: Biblioteca para manipulação de argumentos de linha de comando.

## Instalação

1. Clone este repositório para o seu computador:
   ```bash
   git clone https://github.com/seu-usuario/baixador-videos-youtube.git
Navegue até a pasta do projeto:

bash
Copiar
Editar
cd baixador-videos-youtube
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar
Editar
python -m venv venv
Ative o ambiente virtual:

Windows:
bash
Copiar
Editar
.\venv\Scripts\activate
Linux/Mac:
bash
Copiar
Editar
source venv/bin/activate
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Para executar a aplicação, use o comando:

bash
Copiar
Editar
streamlit run app.py
Como Usar
Execute a aplicação com o comando acima.
Na interface que será aberta em seu navegador, insira a URL do vídeo do YouTube que deseja baixar.
Clique no botão "Baixar 🎥".
O título e o número de visualizações do vídeo serão exibidos.
O vídeo será baixado e salvo na pasta downloads.
Estrutura do Projeto
bash
Copiar
Editar
baixador-videos-youtube/
│
├── app.py               # Arquivo principal da aplicação Streamlit
├── downloads/           # Pasta onde os vídeos baixados serão salvos
├── requirements.txt     # Lista de dependências do projeto
└── README.md            # Este arquivo
Dependências
O projeto depende das seguintes bibliotecas:

pytube: Para fazer o download de vídeos do YouTube.
streamlit: Para criar a interface interativa.
os: Para trabalhar com arquivos e diretórios no sistema.
sys: Para manipular argumentos e variáveis do sistema.
Você pode instalar todas as dependências usando o arquivo requirements.txt com o comando:

bash
Copiar
Editar
pip install -r requirements.txt
Possíveis Melhorias
Implementar uma barra de progresso durante o download.
Permitir a escolha da qualidade do vídeo antes de fazer o download.
Adicionar mais opções, como download de áudio ou playlists.
Contribuindo
Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias ou correções. Se você encontrar algum erro ou tiver sugestões de novos recursos, ficaremos felizes em receber sua contribuição.

