import emoji

mensagem = input("Digite uma mensagem com um código de emoji (ex: :smile:, :heart:): ")

mensagem_com_emoji = emoji.emojize(mensagem, language='alias')

print("Mensagem com emoji:")
print(mensagem_com_emoji)
