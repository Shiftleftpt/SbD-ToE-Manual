#!/usr/bin/env python3
"""
Visual comparison: Human vs Existing vs Robot for the toolchain example
"""

print("\n" + "="*120)
print("🔍 CASE STUDY: Exemplo Toolchain File Analysis")
print("="*120 + "\n")

print("""
FILE: 01-exemplo-toolchain-options.md
PATH: 002-cross-check-normativo/exemplo-playbook/

TOPIC: Practical examples of how to implement different toolchains (Terraform, 
       CloudFormation, Helm) with Kubernetes and AWS.

Content Summary:
  • Terraform + AWS examples (500+ lines)
  • CloudFormation examples (300+ lines)  
  • Helm + Kubernetes examples (300+ lines)
  • Focus on auditability, versioning, security
  • Emphasis on different tool options
  • Infrastructure as Code patterns
  • Central logging collection
  • Vulnerability analysis (SCA/SAST)
""")

print("="*120)
print("PERSPECTIVE 1: 👨 HUMAN ANALYSIS (What a subject matter expert would tag)")
print("="*120 + """

Looking at this document, I would suggest these tags:

DEFINITELY INCLUDE:
  ✓ iac              - Infrastructure as Code is THE main topic
  ✓ toolchain        - Different toolchain options compared
  ✓ ferramentas      - Tools/frameworks are central
  ✓ exemplos         - It's a practical example
  ✓ auditoria        - Audit trails discussed extensively
  ✓ logs             - Centralized logging is a section
  ✓ aws              - Heavy AWS focus (Terraform, CloudFormation, CloudTrail)

STRONGLY CONSIDER:
  • kubernetes       - Helm/K8s section is substantial  
  • deployment       - Different deployment approaches
  • sca              - Vulnerability scanning mentioned
  • terraform        - Specific tool extensively covered
  • helm             - Specific tool extensively covered
  
MAYBE NOT:
  ? vulnerabilidades - Too generic, prefer specific (sca/sast)

TOTAL RECOMMENDATION: 7 core tags + 5 optional = 12 tags
""")

print("="*120)
print("PERSPECTIVE 2: 📋 EXISTING TAGS (Currently in the file)")
print("="*120 + """

Currently has 6 tags:
  1. exemplos        ✓ GOOD - document is example-based
  2. ferramentas     ✓ GOOD - all about tools/frameworks
  3. iac             ✓ GOOD - core topic
  4. logs            ✓ GOOD - logging section
  5. toolchain       ✓ GOOD - toolchain options
  6. vulnerabilidades ⚠️ VAGUE - prefer sca/sast

ANALYSIS:
  • All 6 are relevant
  • Some are important but missing (aws, deployment, kubernetes, auditoria)
  • One tag could be more specific (vulnerabilidades)
""")

print("="*120)
print("PERSPECTIVE 3: 🤖 ROBOT ANALYSIS (What the AI recommends)")
print("="*120 + """

ROBOT FINDINGS (60%+ confidence):

HIGH CONFIDENCE (70% - found exact keyword match):
  + infrastructure      70%  [tag keyword]
  + compliance          70%  [tag keyword]
  + deployment          70%  [tag keyword]  
  + exemplos            70%  [tag keyword]  ✓ ALREADY HAS
  + kubernetes          70%  [tag keyword]
  + terraform           70%  [tag keyword]
  + helm                70%  [tag keyword]
  + segurança           70%  [tag keyword]
  + auditoria           70%  [tag keyword]
  + versioning          70%  [tag keyword]
  + iac                 70%  [tag keyword]  ✓ ALREADY HAS
  + aws                 70%  [tag keyword]
  + toolchain           70%  [tag keyword]  ✓ ALREADY HAS
  + ferramentas         70%  [tag keyword]  ✓ ALREADY HAS
  + logs                70%  [tag keyword]  ✓ ALREADY HAS

MEDIUM CONFIDENCE (50-70%):
  + cloud               60%  [description match; related...]
  + requisitos          60%  [context...]
  ... and 20+ more

ROBOT RE-DETECTION RATE: 5 out of 6 existing tags = 83%
  ✓ Detected: exemplos, iac, toolchain, ferramentas, logs
  ✗ Missed: vulnerabilidades (too abstract)

NEW SUGGESTIONS FROM ROBOT:
  • infrastructure (70%)   - NEW, good suggestion
  • deployment (70%)       - NEW, good suggestion
  • kubernetes (70%)       - NEW, good suggestion
  • terraform (70%)        - NEW, good suggestion
  • helm (70%)             - NEW, good suggestion
  • aws (70%)              - NEW, good suggestion
  • auditoria (70%)        - NEW, good suggestion
""")

print("="*120)
print("FINAL COMPARISON TABLE")
print("="*120 + "\n")

print(f"{'Tag':<20} {'Human':<15} {'Existing':<15} {'Robot 70%+':<20}")
print(f"{'-'*70}")
print(f"{'iac':<20} {'✓ YES':<15} {'✓ YES':<15} {'✓ FOUND':<20}")
print(f"{'toolchain':<20} {'✓ YES':<15} {'✓ YES':<15} {'✓ FOUND':<20}")
print(f"{'ferramentas':<20} {'✓ YES':<15} {'✓ YES':<15} {'✓ FOUND':<20}")
print(f"{'exemplos':<20} {'✓ YES':<15} {'✓ YES':<15} {'✓ FOUND':<20}")
print(f"{'logs':<20} {'✓ YES':<15} {'✓ YES':<15} {'✓ FOUND':<20}")
print(f"{'auditoria':<20} {'✓ YES':<15} {'✗ NO':<15} {'✓ SUGGESTED':<20}")
print(f"{'aws':<20} {'✓ YES':<15} {'✗ NO':<15} {'✓ SUGGESTED':<20}")
print(f"{'deployment':<20} {'✓ YES':<15} {'✗ NO':<15} {'✓ SUGGESTED':<20}")
print(f"{'kubernetes':<20} {'✓ YES':<15} {'✗ NO':<15} {'✓ SUGGESTED':<20}")
print(f"{'terraform':<20} {'~ MAYBE':<15} {'✗ NO':<15} {'✓ SUGGESTED':<20}")
print(f"{'helm':<20} {'~ MAYBE':<15} {'✗ NO':<15} {'✓ SUGGESTED':<20}")
print(f"{'vulnerabilidades':<20} {'⚠️ GENERIC':<15} {'✓ YES':<15} {'✗ NOT FOUND':<20}")

print(f"\n{'='*120}")
print("🎯 CONCLUSIONS")
print(f"{'='*120}\n")

print("""
1. ROBOT AGREES WITH HUMAN (83% accuracy)
   The robot found 5 out of 6 existing tags in the content.
   This shows high recall - the robot understands the document well.

2. ROBOT SUGGESTS IMPROVEMENTS (+7 new tags)
   - aws, deployment, kubernetes, terraform, helm, auditoria
   - These are all STRONGLY supported by content (70% confidence)
   - These are MISSING from current tags but NEEDED for discoverability

3. EXISTING TAG NEEDS REVIEW
   - "vulnerabilidades" is too generic
   - Robot couldn't find it (probably too abstract)
   - Recommendation: Replace with more specific "sca" or "sast"

4. RECOMMENDED ACTION
   KEEP:      exemplos, ferramentas, iac, logs, toolchain (all good)
   REMOVE:    vulnerabilidades (too generic)
   ADD:       aws, deployment, kubernetes, terraform, helm, auditoria
   RESULT:    From 6 tags → 11 tags (more discoverable, more precise)

5. CONFIDENCE LEVEL
   All new suggestions are HIGH CONFIDENCE (70%)
   Robot found exact keyword matches in document
   Safe to add these recommendations
""")

print(f"{'='*120}\n")
