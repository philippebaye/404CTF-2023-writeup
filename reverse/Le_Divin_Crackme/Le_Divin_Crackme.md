# Le Divin Crackme

<img alt="énoncé du challenge" src="enonce.png" width=500>

Le fichier fourni : [divin-crackme](divin-crackme)

On peut retrouver le compilateur utilisé dans la section `.comment` du binaire :

```bash
$ readelf -p .comment divin-crackme

String dump of section '.comment':
  [     0]  GCC: (Debian 12.2.0-14) 12.2.0
```

Le compilateur est donc : `gcc`

La version décompilée de la fonction `main` avec Ghidra est :

```c
undefined8 main(void)
{
  int iVar1;
  size_t sVar2;
  char local_48 [10];
  char acStack_3e [10];
  char acStack_34 [44];
  
  printf("Mot de passe ? : ");
  __isoc99_scanf(&DAT_0010201a,local_48);
  sVar2 = strlen(local_48);
  if ((((sVar2 == 0x1e) && (iVar1 = strncmp(acStack_3e,"Ph13_d4N5_",10), iVar1 == 0)) &&
      (iVar1 = strncmp(local_48,"L4_pH1l0so",10), iVar1 == 0)) &&
     (iVar1 = strncmp(acStack_34,"l3_Cr4cKm3",10), iVar1 == 0)) {
    printf(&DAT_00102040);
    return 0;
  }
  printf(&DAT_00102078);
  return 1;
}
```

Par conséquent la vérification du mot du passe est réalisée via la fonction `strncmp`.

Le mot de passe saisi est stocké dans `local_48` + `acStack_3e` + `acStack_34`.

On peut le vérifier facilement en exécutant le binaire :

```bash
$ ./divin-crackme
Mot de passe ? : L4_pH1l0soPh13_d4N5_l3_Cr4cKm3
Bien joué ! Tu aurais été libre, pour cette fois...
```

Le flag est donc : `404CTF{gcc:strncmp:L4_pH1l0soPh13_d4N5_l3_Cr4cKm3}`
