#!/bin/bash
# More safety, by turning some bugs into errors.
set -o errexit -o pipefail -o nounset

# now enjoy the options in order and nicely split until we see --
# option --output/-o requires 1 argument
LONGOPTS=version:
OPTIONS=

# -temporarily store output to be able to check for errors
# -activate quoting/enhanced mode (e.g. by writing out "--options")
# -pass arguments only via   -- "$@"   to separate them correctly
# -if getopt fails, it complains itself to stdout
PARSED=$(getopt --options=$OPTIONS --longoptions=$LONGOPTS --name "$0" -- "$@") || exit 2
# read getopt's output this way to handle the quoting right:
eval set -- "$PARSED"
unset PARSED


while true; do
    case "$1" in
        --version)
            version="$2"
            shift 2
            ;;
        --)
            shift
            break
            ;;
        *)
            echo "Programming error"
            exit 3
            ;;
    esac
done

echo "+ version=$version"

# zip needed files
tar czf v$version.tar.gz hdl/ef_util_lib.v fw
# get checksum
shasum -a 256 v$version.tar.gz > v$version.tar.gz.sha256

# create tag
git tag -a EF_IP_UTIL-v$version -m "Release version $version"
git push origin EF_IP_UTIL-v$version

# create release
set -x
if gh release view EF_IP_UTIL-v$version > /dev/null 2>&1; then
    echo "Release EF_IP_UTIL-v$version already exists. Skipping..."
else
    echo "Creating release EF_IP_UTIL-v$version..."
    gh release create EF_IP_UTIL-v$version v$version.tar.gz -t "EF_IP_UTIL-v$version" --notes "sha256: $(cat v$version.tar.gz.sha256)"
fi