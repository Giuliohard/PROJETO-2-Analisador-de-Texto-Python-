import re
from collections import Counter
import string

class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.words = self._extract_words()
    
    def _extract_words(self):
        """Extrai palavras do texto, removendo pontuação"""
        if not self.text or not self.text.strip():
            return []
        
        text_no_punct = self.text.translate(str.maketrans('', '', string.punctuation))
        words = text_no_punct.lower().split()
        return [word for word in words if word.strip()]
    
    def word_count(self):
        """Retorna o número total de palavras"""
        return len(self.words)
    
    def character_count(self, include_spaces=True):
        """Retorna o número de caracteres"""
        if not self.text:
            return 0
        if include_spaces:
            return len(self.text)
        return len(self.text.replace(" ", ""))
    
    def sentence_count(self):
        """Retorna o número de frases"""
        if not self.text:
            return 0
        sentences = re.split(r'[.!?]+', self.text)
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)
    
    def most_common_words(self, n=10):
        """Retorna as N palavras mais comuns"""
        if not self.words:
            return []
        word_counts = Counter(self.words)
        return word_counts.most_common(n)
    
    def average_word_length(self):
        """Retorna o comprimento médio das palavras"""
        if not self.words:
            return 0
        total_length = sum(len(word) for word in self.words)
        return round(total_length / len(self.words), 2)
    
    def reading_time(self, words_per_minute=200):
        """Calcula o tempo estimado de leitura"""
        if not self.words:
            return 0
        minutes = len(self.words) / words_per_minute
        return round(max(minutes, 0.1), 1)  # Mínimo de 0.1 minuto
    
    def vocabulary_richness(self):
        """Calcula a riqueza vocabular"""
        if not self.words:
            return 0
        unique_words = len(set(self.words))
        return round(unique_words / len(self.words) * 100, 2)
    
    def get_text_preview(self, max_length=100):
        """Retorna uma prévia do texto"""
        if not self.text:
            return "Nenhum texto carregado"
        if len(self.text) <= max_length:
            return self.text
        return self.text[:max_length] + "..."
    
    def generate_detailed_report(self):
        """Gera um relatório completo da análise"""
        if not self.text:
            return "❌ Nenhum texto disponível para análise."
        
        report = []
        report.append("🎯 RELATÓRIO COMPLETO DE ANÁLISE")
        report.append("=" * 55)
        report.append(f"📝 Total de palavras: {self.word_count():,}")
        report.append(f"🔤 Caracteres (com espaços): {self.character_count():,}")
        report.append(f"🔡 Caracteres (sem espaços): {self.character_count(False):,}")
        report.append(f"📄 Total de frases: {self.sentence_count()}")
        report.append(f"📏 Média de caracteres por palavra: {self.average_word_length()}")
        report.append(f"⏱️ Tempo de leitura estimado: {self.reading_time()} minutos")
        report.append(f"🎯 Riqueza vocabular: {self.vocabulary_richness()}%")
        report.append(f"📋 Palavras únicas: {len(set(self.words)):,}")
        
        report.append("\n🔝 TOP 10 PALAVRAS MAIS FREQUENTES:")
        report.append("-" * 40)
        common_words = self.most_common_words(10)
        if common_words:
            for i, (word, count) in enumerate(common_words, 1):
                percentage = (count / len(self.words)) * 100
                report.append(f"  {i:2d}. {word:<15} → {count:3d} vezes ({percentage:.1f}%)")
        else:
            report.append("  Nenhuma palavra encontrada.")
        
        report.append(f"\n📄 PRÉVIA DO TEXTO:")
        report.append("-" * 30)
        report.append(f'"{self.get_text_preview(150)}"')
        
        return "\n".join(report)
    
    def generate_quick_report(self):
        """Gera um relatório rápido"""
        if not self.text:
            return "❌ Nenhum texto disponível."
        
        report = []
        report.append("📊 RESUMO RÁPIDO:")
        report.append(f"• Palavras: {self.word_count():,}")
        report.append(f"• Caracteres: {self.character_count():,}")
        report.append(f"• Frases: {self.sentence_count()}")
        report.append(f"• Tempo de leitura: {self.reading_time()} min")
        report.append(f"• Riqueza vocabular: {self.vocabulary_richness()}%")
        
        return "\n".join(report)
