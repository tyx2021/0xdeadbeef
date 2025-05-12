#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main() {
    //Ignore
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    printf("Someone added this to my code... (*(void(*)()) input)(); What???\n");

    gid_t gid = getegid();
    setresgid(gid, gid, gid);

    char shell[105];
    scanf("%100s", shell);
    ((void(*)()) shell)();

    return 0;
}