from search import search_prompt

def main():
    print("Chat iniciado! Digite 'sair' para encerrar.\n")

    while True:
        user_input = input("Pergunta: ")

        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Encerrando o chat...")
            break

        try:
            response = search_prompt(user_input)
            print(f"Resposta: {response}\n")
        except Exception as e:
            print(f"Ocorreu um erro ao processar sua mensagem: {e}\n")

if __name__ == "__main__":
    main()