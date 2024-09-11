import streamlit as st
import contrato
from datetime import datetime, time

def main():
    
    st.title("Sistema de CRM e Vendas da Zapflow - Frontend Simples")
    email = st.text_input("Campo de texto para inserção do e-mail")
    data = st.date_input("Data da Compra", datetime.now())
    hora = st.time_input("Hora da Compra", value=time(9, 0)) #Padrão: 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produto = st.selectbox("Produto", options=["Zapflow com Gemini", "Zapflow com ChatGPT", "Zapflow com Llama"])
    
    if st.button("Salvar"):
        
        data_hora = datetime.combine(data, hora)
        st.write("**Dados da Venda:**")
        st.write(f"Email do Vendedos: {email}")
        st.write(f"Data e hora da Compra: {data_hora}")
        st.write(f"Valor da Venda: R$ {valor:.2f}")
        st.write(f"Quantidade de Produtos: {quantidade}")
        st.write(f"Produto: {produto}")
    
if __name__ == "__main__":
    main()
    