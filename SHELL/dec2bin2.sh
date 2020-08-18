#! /bin/sh

E=[24680] # even nums
O=[13579] # odd  nums

lookuptbl() {
   case $1 in
      $E[01]* ) echo 0 ;; $E[23]* ) echo 1 ;;
      $E[45]* ) echo 2 ;; $E[67]* ) echo 3 ;;
      $E[89]* ) echo 4 ;; $O[01]* ) echo 5 ;;
      $O[23]* ) echo 6 ;; $O[45]* ) echo 7 ;;
      $O[67]* ) echo 8 ;; $O[89]* ) echo 9 ;;
   esac
}

divby2() {
   set -- "0$1"

   while case $1 in ? ) break ;; esac; do
      set -- "${1#?}" "${2-}$(lookuptbl "$1")"
   done

   echo $2
}

dec2bin() {
   case $1 in *[!0]* ) :;; * ) echo 0; return ;; esac

   while :
   do
      case $1 in *[!0]* ) :;; * ) break;; esac
      case $1 in
         *$E ) set -- "$(divby2 "$1")" "0${2-}" ;;
         *$O ) set -- "$(divby2 "$1")" "1${2-}" ;;
      esac
   done

   echo "$2"
}

# And then... (assuming pure number given from command line)
num=${1:-304}
dec2bin "$num"
