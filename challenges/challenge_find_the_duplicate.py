def find_duplicate(nums):
    # Verifica se a entrada é uma lista não vazia
    if not isinstance(nums, list) or len(nums) < 2:
        return False

    # Verifica se todos os elementos são inteiros positivos
    if not all(isinstance(num, int) and num > 0 for num in nums):
        return False

    # Conjunto para rastrear os elementos já vistos
    seen = set()

    for num in nums:
        # Se o número já foi visto, é o duplicado
        if num in seen:
            return num
        seen.add(num)

    # Se não houver duplicados, retorna False
    return False
