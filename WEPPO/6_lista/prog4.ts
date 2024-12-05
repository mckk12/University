import { Bar } from './help';

import MyDefaultClass from './help';

new Bar();
new MyDefaultClass();

// Eksport nazwany pozwala na eksportowanie wielu wartości z modułu. Każda z tych wartości ma swoją unikalną nazwę.
// Importowanie z eksportu nazwanego wymaga użycia tych samych nazw w klamrach {}.

// Eksport domyślny pozwala na eksportowanie tylko jednej wartości (funkcji, klasy, obiektu, etc.) z modułu. Nie musi ona mieć nazwy.
// Importowanie z eksportu domyślnego nie wymaga klamr {} i możemy użyć dowolnej nazwy.

