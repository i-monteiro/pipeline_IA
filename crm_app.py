import streamlit as st
from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError
from database import salvar_no_postgres

def main():
    
    st.title("Sistema de CRM e Vendas")
    email = st.text_input("Campo de texto para inserção do e-mail")
    data = st.date_input("Data da Compra", datetime.now())
    hora = st.time_input("Hora da Compra", value=time(9, 0))  # Padrão: 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produto = st.selectbox("Produto", options=["Zapflow com Gemini", "Zapflow com ChatGPT", "Zapflow com Llama"])
    
    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data, hora)           
            venda = Vendas(
                email=email,
                data=data_hora,
                valor=valor,
                quantidade=quantidade,
                produto=produto
            )
            st.write(venda)
            salvar_no_postgres(venda)
        
        except ValidationError as e:
            st.error(f"Erro de validação: {e}")
if __name__ == "__main__":
    main()
