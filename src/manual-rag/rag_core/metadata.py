"""Metadata parsing and enrichment for RAG infrastructure

Understands the structure of the manual:
- Chapter organization (000, 001, 002, 003, 010...)
- Security domains within chapters
- File path patterns and their meaning
"""

from typing import Dict


class ChaptersMetadata:
    """Parse and understand chapter structure of the manual"""
    
    CHAPTER_PATTERNS = {
        "000-teory-of-everything": {"name": "Theory of Everything", "type": "foundational"},
        "001-how-to-manual": {"name": "How to Use Manual", "type": "meta"},
        "002-cross-check-normativo": {"name": "Normative Cross-Check", "type": "frameworks"},
        "003-policies-globals": {"name": "Global Policies", "type": "governance"},
        "010-sbd-manual": {"name": "Security by Design Manual", "type": "main_content"},
    }
    
    SECURITY_DOMAINS = {
        "01-classificacao-aplicacoes": "Application Classification",
        "02-requisitos-seguranca": "Security Requirements",
        "03-threat-modeling": "Threat Modeling",
        "04-arquitetura-segura": "Secure Architecture",
        "05-dependencias-sbom-sca": "Dependencies & SBOM",
        "06-desenvolvimento-seguro": "Secure Development",
        "07-cicd-seguro": "Secure CI/CD",
        "08-iac-infraestrutura": "Infrastructure as Code",
        "09-containers-imagens": "Containers & Images",
        "10-testes-seguranca": "Security Testing",
        "11-deploy-seguro": "Secure Deployment",
        "12-monitorizacao-operacoes": "Monitoring & Operations",
        "13-formacao-onboarding": "Training & Onboarding",
        "14-governanca-contratacao": "Governance & Procurement",
    }
    
    @staticmethod
    def parse_path(file_path: str) -> Dict:
        """Extract structured metadata from file path
        
        Example paths:
        - 010-sbd-manual/02-requisitos-seguranca/intro.md
        - 002-cross-check-normativo/dora/01-intro.md
        - 000-teory-of-everything/01-intro.md
        
        Args:
            file_path: Relative path from manual root
            
        Returns:
            Dictionary with parsed metadata
        """
        parts = file_path.replace(".md", "").split("/")
        
        metadata = {
            "file_path": file_path,
            "file_name": parts[-1] if parts else "",
            "chapter": parts[0] if parts else "",
            "section": parts[1] if len(parts) > 1 else "",
            "subsection": parts[2] if len(parts) > 2 else "",
        }
        
        # Enrich with chapter info
        if metadata["chapter"] in ChaptersMetadata.CHAPTER_PATTERNS:
            ch_info = ChaptersMetadata.CHAPTER_PATTERNS[metadata["chapter"]]
            metadata["chapter_name"] = ch_info["name"]
            metadata["chapter_type"] = ch_info["type"]
        
        # Enrich with security domain info (only for 010-sbd-manual)
        if metadata["chapter"] == "010-sbd-manual" and metadata["section"]:
            if metadata["section"] in ChaptersMetadata.SECURITY_DOMAINS:
                metadata["domain"] = ChaptersMetadata.SECURITY_DOMAINS[metadata["section"]]
        
        return metadata
