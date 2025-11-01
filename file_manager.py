import os
import json
from datetime import datetime

class FileManager:
    @staticmethod
    def load_text_file(filename):
        """Carrega texto de um arquivo com múltiplos encodings"""
        encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']
        
        for encoding in encodings:
            try:
                with open(filename, 'r', encoding=encoding) as file:
                    content = file.read()
                    if content.strip():
                        print(f"✅ Arquivo carregado com encoding: {encoding}")
                        return content
            except UnicodeDecodeError:
                continue
            except FileNotFoundError:
                return None
            except Exception as e:
                print(f"❌ Erro com encoding {encoding}: {e}")
                continue
        
        print("❌ Não foi possível ler o arquivo com nenhum encoding suportado.")
        return None
    
    @staticmethod
    def save_analysis_result(text, analysis_data, filename=None):
        """Salva o resultado da análise em um arquivo"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"analise_texto_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write("RESULTADO DA ANÁLISE DE TEXTO\n")
                file.write("=" * 50 + "\n")
                file.write(f"Data da análise: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
                file.write(f"Arquivo: {filename}\n")
                file.write("\n" + analysis_data + "\n")
                file.write("\n" + "=" * 50 + "\n")
                file.write("TEXTO ANALISADO:\n")
                file.write("=" * 50 + "\n")
                file.write(text[:5000] + ("..." if len(text) > 5000 else ""))
            
            print(f"✅ Resultado salvo em: {filename}")
            return True
        except Exception as e:
            print(f"❌ Erro ao salvar arquivo: {e}")
            return False
    
    @staticmethod
    def list_text_files(directory="."):
        """Lista arquivos .txt no diretório"""
        try:
            files = [f for f in os.listdir(directory) 
                    if f.endswith('.txt') and os.path.isfile(os.path.join(directory, f))]
            return sorted(files)
        except Exception as e:
            print(f"❌ Erro ao listar arquivos: {e}")
            return []
