import socket

def printer(ip, file):
    # Cria um socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Conecta ao endereço IP da impressora na porta 9100 (porta padrão para comunicação com impressoras)
        sock.connect((ip, 9100))
        
        # Lê o conteúdo do arquivo a ser impresso
        with open(file, 'rb') as f:
            content = f.read()
        
        # Envia o conteúdo para a impressora
        sock.sendall(content)
        
        print("Documento enviado para impressão com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar documento para impressora: {e}")
    finally:
        # Fecha o socket
        sock.close()

# Exemplo de uso
if __name__ == "__main__":
    ip = '192.168.1.100'  # IP da impressora na rede
    file = 'document.pdf'  # Nome do arquivo a ser impresso
    printer(ip, file)
