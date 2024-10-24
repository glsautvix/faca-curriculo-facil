import streamlit as st



def render_screen():
    """ This function renders the help screen """
    st.title("Ajuda")
    st.markdown("## Como usar o aplicativo")
    st.markdown("### 1. Crie um currículo")
    st.markdown("Para criar um currículo, clique na aba 'Criar currículo' e preencha os campos com suas informações.")
    st.markdown("### 2. Visualize o currículo")
    st.markdown("Para visualizar o currículo que você acabou de criar, clique na aba 'Visualizar currículo'.")
    st.markdown("### 3. Salve o currículo")
    st.markdown("Para salvar o currículo que você acabou de criar, clique no botão 'Salvar' na aba 'Visualizar currículo'.")
    st.markdown("### 4. Carregue um currículo")
    st.markdown("Para carregar um currículo que você já criou, clique na aba 'Carregar currículo' e selecione o arquivo que deseja carregar.")
    st.markdown("### 5. Exporte o currículo")
    st.markdown("Para exportar o currículo que você acabou de criar, clique no botão 'Exportar' na aba 'Visualizar currículo'.")
    st.markdown("### 6. Configurações")
    st.markdown("Para acessar as configurações do aplicativo, clique na aba 'Configurações'.")
    st.markdown("### 7. Ajuda")
    st.markdown("Para acessar a ajuda do aplicativo, clique na aba 'Ajuda'.")
    st.markdown("### 8. Sobre")
    st.markdown("Para saber mais sobre o aplicativo, clique na aba 'Sobre'.")
    