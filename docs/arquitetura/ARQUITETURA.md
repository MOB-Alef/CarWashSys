# ARQUITETURA DO CARWASHSYS

## Objetivo

Este documento descreve a arquitetura geral do CarWashSys.

Seu objetivo é apresentar como os módulos se relacionam, quais são suas responsabilidades e como o sistema foi organizado para facilitar sua manutenção e evolução.

---

## Visão Geral

O CarWashSys foi desenvolvido utilizando o framework Django, seguindo uma arquitetura baseada em módulos (Apps).

Cada módulo possui uma responsabilidade específica, permitindo que o sistema cresça de forma organizada.

---

## Estrutura Geral do Sistema

Dashboard
│
├── Accounts
├── Clientes
│   └── Veículos
│
├── Ordens de Serviço
│   ├── Estoque
│   ├── Financeiro
│   └── Funcionários