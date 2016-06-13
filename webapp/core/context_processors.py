def empresa(request):
    return {
        'empresa': dict(
                rua='Rua Cardamon Place',
                numero='3000',
                bairro='Centro',
                cep='00000-000',
                cidade='Ciudad Del Este',
                uf='SC',
                email='contato@cinepro.com',
                telefone='+11 11 1111 1111',
                whatsapp='+11 11 1111 1111',
                instagram='',
                facebook='#',
                twitter='#',
                latitude='-26.3835133',
                longitude='-53.5277792',
        )
    }