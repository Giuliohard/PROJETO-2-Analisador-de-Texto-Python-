from text_analyzer import TextAnalyzer
from file_manager import FileManager
import os

class TextAnalyzerApp:
    def __init__(self):
        self.current_text = ""
        self.analyzer = None
    
    def clear_screen(self):
        """Limpa a tela do terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        """Exibe o cabeçalho da aplicação"""
        print("🎯" + "="*60 + "🎯")
        print("           ANALISADOR DE TEXTO AVANÇADO - GIULIO MARCO")
        print("🎯" + "="*60 + "🎯")
        
        if self.current_text:
            preview = self.analyzer.get_text_preview(80) if self.analyzer else "Nenhum"
            print(f"📄 Texto atual: {preview}")
            print(f"📊 Estatísticas: {len(self.current_text):,} chars")
        print()
    
    def wait_for_enter(self):
        """Aguarda o usuário pressionar Enter"""
        input("\n↵ Pressione ENTER para continuar...")
    
    def get_text_input(self):
        """Obtém texto do usuário"""
        print("\n📝 DIGITE OU COLE SEU TEXTO:")
        print("💡 Dica: Cole todo o texto de uma vez")
        print("   Pressione Enter duas vezes para finalizar")
        print("-" * 50)
        
        lines = []
        empty_lines = 0
        
        while True:
            try:
                line = input()
                if line.strip() == "":
                    empty_lines += 1
                    if empty_lines >= 2 and lines:
                        break
                    elif not lines:
                        continue
                else:
                    empty_lines = 0
                    lines.append(line)
            except KeyboardInterrupt:
                print("\n❌ Entrada cancelada.")
                return None
            except EOFError:
                break
        
        text = "\n".join(lines)
        
        if not text.strip():
            print("❌ Nenhum texto foi inserido.")
            return None
        
        print(f"✅ Texto recebido: {len(text):,} caracteres, {len(text.split()):,} palavras")
        return text
    
    def load_file_menu(self):
        """Menu para carregar arquivo"""
        print("\n📁 CARREGAR ARQUIVO .TXT")
        print("-" * 30)
        
        # Lista arquivos .txt disponíveis
        text_files = FileManager.list_text_files()
        if text_files:
            print("📂 Arquivos .txt encontrados:")
            for i, filename in enumerate(text_files, 1):
                print(f"  {i}. {filename}")
            print(f"  {len(text_files) + 1}. Digitar nome manualmente")
        else:
            print("📂 Nenhum arquivo .txt encontrado no diretório atual")
            print(" 1. Digitar nome manualmente")
        
        choice = input("\n🎯 Escolha uma opção: ").strip()
        
        if text_files and choice.isdigit() and 1 <= int(choice) <= len(text_files):
            filename = text_files[int(choice) - 1]
        else:
            filename = input("📁 Digite o nome do arquivo .txt: ").strip()
            if not filename.endswith('.txt'):
                filename += '.txt'
        
        content = FileManager.load_text_file(filename)
        if content:
            self.current_text = content
            self.analyzer = TextAnalyzer(self.current_text)
            print(f"✅ Arquivo '{filename}' carregado com sucesso!")
            return True
        else:
            print("❌ Não foi possível carregar o arquivo.")
            return False
    
    def analyze_current_text(self):
        """Analisa o texto atual"""
        if not self.current_text:
            print("❌ Nenhum texto carregado para análise.")
            return
        
        print("\n🔍 ANALISANDO TEXTO...")
        print("⏳ Isso pode levar alguns segundos para textos longos...")
        
        report = self.analyzer.generate_detailed_report()
        print("\n" + report)
        
        # Oferece para salvar o resultado
        save = input("\n💾 Deseja salvar este relatório? (s/N): ").strip().lower()
        if save in ['s', 'sim', 'y', 'yes']:
            filename = input("📁 Nome do arquivo (ou Enter para automático): ").strip()
            if not filename:
                filename = None
            FileManager.save_analysis_result(self.current_text, report, filename)
    
    def quick_analysis_menu(self):
        """Menu de análise rápida"""
        if not self.current_text:
            print("❌ Nenhum texto carregado.")
            return
        
        quick_report = self.analyzer.generate_quick_report()
        print("\n" + quick_report)
        
        # Mostra palavras mais comuns
        common_words = self.analyzer.most_common_words(5)
        if common_words:
            print("\n🔝 TOP 5 PALAVRAS:")
            for i, (word, count) in enumerate(common_words, 1):
                print(f"  {i}. '{word}' → {count} vezes")
    
    def main_menu(self):
        """Menu principal da aplicação"""
        while True:
            self.clear_screen()
            self.display_header()
            
            print("📋 MENU PRINCIPAL:")
            print("=" * 30)
            print("1. 📝 Inserir texto manualmente")
            print("2. 📁 Carregar arquivo .txt")
            
            if self.current_text:
                print("3. 🔍 Análise completa")
                print("4. 📊 Análise rápida")
                print("5. 🗑️  Limpar texto atual")
                print("6. 🚪 Sair")
            else:
                print("3. 🚪 Sair")
            
            choice = input("\n🎯 Escolha uma opção: ").strip()
            
            if choice == "1":
                text = self.get_text_input()
                if text:
                    self.current_text = text
                    self.analyzer = TextAnalyzer(self.current_text)
                self.wait_for_enter()
            
            elif choice == "2":
                self.load_file_menu()
                self.wait_for_enter()
            
            elif choice == "3" and self.current_text:
                self.analyze_current_text()
                self.wait_for_enter()
            
            elif choice == "4" and self.current_text:
                self.quick_analysis_menu()
                self.wait_for_enter()
            
            elif choice == "5" and self.current_text:
                self.current_text = ""
                self.analyzer = None
                print("✅ Texto atual limpo!")
                self.wait_for_enter()
            
            elif choice == "6" and self.current_text:
                print("👋 Obrigado por usar o Analisador de Texto!")
                break
            
            elif choice == "3" and not self.current_text:
                print("👋 Obrigado por usar o Analisador de Texto!")
                break
            
            else:
                print("❌ Opção inválida. Tente novamente.")
                self.wait_for_enter()

def main():
    """Função principal"""
    app = TextAnalyzerApp()
    app.main_menu()

if __name__ == "__main__":
    main()
