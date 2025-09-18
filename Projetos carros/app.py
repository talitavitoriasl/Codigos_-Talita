import streamlit as st
###### COLOCA UM TITULO
#st.title("Imune ao conhecimento")
########## ESCREVER
#st.write("Testando.....Esquerda e Direita ")
###### BARRA LATERAL
#st. sidebar. title("Barra lateral")
##### CRIANDO A LISTA
#nomes =["Pedro tcholão", " Wender Motoca", "Izaias michael jackson", "Ederson alérgico ao ensino e leitura"]
###### CRIA A CAIXINHA NA BARRA LATERAL
#st. sidebar. selectbox("Escolha um nome ;" , nomes)
         
#st.video("https://www.youtube.com/watch?v=eCl2XRzMH28")


st.sidebar.title("Aluguel de carros")
st.sidebar.image("logo.png")
st.sidebar.write("Escolha o carro ideal para você!")
carros = ["Tesla","BMW","bugatti","Lamborghini Aventor"]
opcao = st.sidebar.selectbox("Selecione o modelo do carro:", carros)
          

#--------------------------------- Principal
st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')


### Copia daqui pra frente --- Defina a diária
if opcao == 'BMW' :
    diaria = 450

elif opcao =='Tesla' :
    diaria = 500

elif opcao == 'bugatti' :
    diaria = 900

elif opcao == 'Lamborghini Aventor' :
    diaria = 1.000


### calcular

if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias + total_km

    st.warning(f'Você alugou o {opcao} por  {dias} dias e rodou {km} km. O valor total a pagar é r${aluguel_total:2f}')