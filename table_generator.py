"""
Table Generator Utility for Comparison & Difference Detection
Automatically generates HTML tables for comparison/difference questions
"""

import re
from typing import Dict, List, Tuple, Optional

class TableDetector:
    """Detects if a query is about comparison or difference"""
    
    # Keywords that indicate comparison/difference questions
    COMPARISON_KEYWORDS = {
        'compare', 'comparison', 'versus', 'vs', 'compared to', 'compared with',
        'difference', 'differences', 'different from', 'distinguish', 'distinction',
        'contrast', 'contrasted with', 'similar', 'similarities', 'pros and cons',
        'advantages and disadvantages', 'benefits vs', 'which is better',
        'what\'s the difference', 'how are they different', 'like vs'
    }
    
    def __init__(self, confidence_threshold: float = 0.6):
        """
        Initialize the detector
        
        Args:
            confidence_threshold: Minimum confidence score (0-1) to generate table
        """
        self.confidence_threshold = confidence_threshold
    
    def detect_comparison_question(self, query: str) -> Tuple[bool, float]:
        """
        Detect if query is about comparison/difference
        
        Args:
            query: The user's question
            
        Returns:
            Tuple of (is_comparison, confidence_score)
        """
        query_lower = query.lower().strip()
        
        # Check for exact keyword matches
        matched_keywords = []
        for keyword in self.COMPARISON_KEYWORDS:
            if keyword in query_lower:
                matched_keywords.append(keyword)
        
        # Calculate confidence based on keyword matches
        if not matched_keywords:
            return False, 0.0
        
        # Higher confidence with more keywords found
        confidence = min(len(matched_keywords) * 0.3, 1.0)
        
        # Boost confidence for strong phrases
        strong_phrases = ['compare', 'difference', 'versus', 'vs', 'contrast']
        if any(phrase in query_lower for phrase in strong_phrases):
            confidence = min(confidence + 0.3, 1.0)
        
        is_comparison = confidence >= self.confidence_threshold
        return is_comparison, confidence
    
    def get_detected_keywords(self, query: str) -> List[str]:
        """Get list of detected keywords from query"""
        query_lower = query.lower()
        return [kw for kw in self.COMPARISON_KEYWORDS if kw in query_lower]


class HTMLTableGenerator:
    """Generates HTML tables for comparison responses"""
    
    @staticmethod
    def create_comparison_table(
        title: str,
        items: List[str],
        attributes: List[str],
        data: Dict[str, Dict[str, str]],
        theme: str = "beige"
    ) -> str:
        """
        Create a structured comparison table
        
        Args:
            title: Table title
            items: List of items being compared
            attributes: List of attributes to compare
            data: Dictionary with structure: {item: {attribute: value}}
            theme: Color theme (beige, green, blue)
            
        Returns:
            HTML string for the table
        """
        
        # Define theme colors
        themes = {
            "beige": {"header": "#BEFF3F", "row1": "#F5F3ED", "row2": "#EDE9DC"},
            "green": {"header": "#A8E71F", "row1": "#E8F5E9", "row2": "#F1F8E9"},
            "blue": {"header": "#64B5F6", "row1": "#E3F2FD", "row2": "#BBDEFB"}
        }
        
        colors = themes.get(theme, themes["beige"])
        
        # Build table HTML
        html = f"""
        <div style="margin: 1.5rem 0; overflow-x: auto;">
            <h3 style="color: #2a2a2a; font-size: 1.2rem; margin-bottom: 1rem;">
                📊 {title}
            </h3>
            <table style="
                width: 100%;
                border-collapse: collapse;
                border: 1px solid #E8E4D4;
                border-radius: 8px;
                overflow: hidden;
                background: white;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
                font-family: 'Poppins', sans-serif;
            ">
                <thead>
                    <tr style="background: {colors['header']}; color: #1a1a1a;">
                        <th style="
                            padding: 1rem;
                            text-align: left;
                            font-weight: 700;
                            border-bottom: 2px solid #E8E4D4;
                        ">Feature</th>
        """
        
        # Add item headers
        for item in items:
            html += f"""
                        <th style="
                            padding: 1rem;
                            text-align: left;
                            font-weight: 700;
                            border-bottom: 2px solid #E8E4D4;
                        ">{item}</th>
            """
        
        html += """
                    </tr>
                </thead>
                <tbody>
        """
        
        # Add rows
        for idx, attribute in enumerate(attributes):
            row_color = colors['row1'] if idx % 2 == 0 else colors['row2']
            html += f"""
                    <tr style="background: {row_color};">
                        <td style="
                            padding: 1rem;
                            font-weight: 600;
                            color: #2a2a2a;
                            border-bottom: 1px solid #E8E4D4;
                        ">{attribute}</td>
            """
            
            for item in items:
                value = data.get(item, {}).get(attribute, "-")
                html += f"""
                        <td style="
                            padding: 1rem;
                            color: #2a2a2a;
                            border-bottom: 1px solid #E8E4D4;
                        ">{value}</td>
                """
            
            html += """
                    </tr>
            """
        
        html += """
                </tbody>
            </table>
        </div>
        """
        
        return html
    
    @staticmethod
    def create_pros_cons_table(
        item1: str,
        pros1: List[str],
        cons1: List[str],
        item2: str,
        pros2: List[str],
        cons2: List[str]
    ) -> str:
        """
        Create a pros/cons comparison table
        
        Returns:
            HTML string for the table
        """
        
        html = f"""
        <div style="margin: 1.5rem 0;">
            <h3 style="color: #2a2a2a; font-size: 1.2rem; margin-bottom: 1rem;">
                ⚖️ Pros & Cons Comparison
            </h3>
            <table style="
                width: 100%;
                border-collapse: collapse;
                border: 1px solid #E8E4D4;
                background: white;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
                font-family: 'Poppins', sans-serif;
            ">
                <thead>
                    <tr style="background: #BEFF3F; color: #1a1a1a;">
                        <th colspan="2" style="
                            padding: 1rem;
                            font-weight: 700;
                            border-bottom: 2px solid #E8E4D4;
                            text-align: center;
                        ">{item1}</th>
                        <th colspan="2" style="
                            padding: 1rem;
                            font-weight: 700;
                            border-bottom: 2px solid #E8E4D4;
                            text-align: center;
                        ">{item2}</th>
                    </tr>
                    <tr style="background: #EDE9DC;">
                        <th style="
                            padding: 0.75rem;
                            font-weight: 600;
                            border-bottom: 1px solid #E8E4D4;
                            width: 25%;
                        ">✅ Pros</th>
                        <th style="
                            padding: 0.75rem;
                            font-weight: 600;
                            border-bottom: 1px solid #E8E4D4;
                            width: 25%;
                        ">❌ Cons</th>
                        <th style="
                            padding: 0.75rem;
                            font-weight: 600;
                            border-bottom: 1px solid #E8E4D4;
                            width: 25%;
                        ">✅ Pros</th>
                        <th style="
                            padding: 0.75rem;
                            font-weight: 600;
                            border-bottom: 1px solid #E8E4D4;
                            width: 25%;
                        ">❌ Cons</th>
                    </tr>
                </thead>
                <tbody>
        """
        
        # Get max rows
        max_rows = max(len(pros1), len(cons1), len(pros2), len(cons2))
        
        for i in range(max_rows):
            bg_color = "#F5F3ED" if i % 2 == 0 else "#EDE9DC"
            html += f'<tr style="background: {bg_color};">'
            
            # Item 1 Pro
            if i < len(pros1):
                html += f"""
                    <td style="
                        padding: 0.75rem;
                        border-bottom: 1px solid #E8E4D4;
                        color: #2a2a2a;
                    ">• {pros1[i]}</td>
                """
            else:
                html += '<td style="padding: 0.75rem; border-bottom: 1px solid #E8E4D4;"></td>'
            
            # Item 1 Con
            if i < len(cons1):
                html += f"""
                    <td style="
                        padding: 0.75rem;
                        border-bottom: 1px solid #E8E4D4;
                        color: #2a2a2a;
                    ">• {cons1[i]}</td>
                """
            else:
                html += '<td style="padding: 0.75rem; border-bottom: 1px solid #E8E4D4;"></td>'
            
            # Item 2 Pro
            if i < len(pros2):
                html += f"""
                    <td style="
                        padding: 0.75rem;
                        border-bottom: 1px solid #E8E4D4;
                        color: #2a2a2a;
                    ">• {pros2[i]}</td>
                """
            else:
                html += '<td style="padding: 0.75rem; border-bottom: 1px solid #E8E4D4;"></td>'
            
            # Item 2 Con
            if i < len(cons2):
                html += f"""
                    <td style="
                        padding: 0.75rem;
                        border-bottom: 1px solid #E8E4D4;
                        color: #2a2a2a;
                    ">• {cons2[i]}</td>
                """
            else:
                html += '<td style="padding: 0.75rem; border-bottom: 1px solid #E8E4D4;"></td>'
            
            html += '</tr>'
        
        html += """
                </tbody>
            </table>
        </div>
        """
        
        return html


# Example usage
if __name__ == "__main__":
    # Initialize detector
    detector = TableDetector()
    
    # Test queries
    test_queries = [
        "Compare Python and JavaScript",
        "What's the difference between iOS and Android?",
        "Compare machine learning vs deep learning",
        "Tell me about artificial intelligence",  # Should NOT generate table
        "Pros and cons of remote work vs office",
    ]
    
    print("=" * 60)
    print("COMPARISON DETECTION TEST")
    print("=" * 60)
    
    for query in test_queries:
        is_comp, confidence = detector.detect_comparison_question(query)
        keywords = detector.get_detected_keywords(query)
        print(f"\nQuery: {query}")
        print(f"Is Comparison: {is_comp} (Confidence: {confidence:.2f})")
        print(f"Keywords: {keywords}")
    
    # Test table generation
    print("\n" + "=" * 60)
    print("TABLE GENERATION EXAMPLE")
    print("=" * 60)
    
    # Example: Compare Python vs JavaScript
    data = {
        "Python": {
            "Type": "Interpreted",
            "Speed": "Medium",
            "Use Case": "Data Science, Backend",
            "Learning Curve": "Beginner-friendly"
        },
        "JavaScript": {
            "Type": "Interpreted/JIT",
            "Speed": "Fast",
            "Use Case": "Frontend, Full-stack",
            "Learning Curve": "Moderate"
        }
    }
    
    table_html = HTMLTableGenerator.create_comparison_table(
        title="Python vs JavaScript",
        items=["Python", "JavaScript"],
        attributes=["Type", "Speed", "Use Case", "Learning Curve"],
        data=data,
        theme="beige"
    )
    
    print("\nGenerated Table HTML:")
    print(table_html)