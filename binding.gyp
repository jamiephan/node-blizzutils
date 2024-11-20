{
    "targets": [
        {
            "target_name": "casclib-native",
            "sources": [
                "src/native/node-casclib/main.cc",
                "src/native/node-casclib/bindings/BCascOpenStorageEx.cc"
            ],
            "include_dirs": [
                "<!@(node -p \"require(\\\"node-addon-api\\\").include\")"
            ],
            "dependencies": [
                "<!(node -p \"require(\\\"node-addon-api\\\").gyp\")",
                "deps-casclib"
            ],
            "cflags!": [
                "-fno-exceptions"
            ],
            "cflags_cc!": [
                "-fno-exceptions"
            ],
            "xcode_settings": {
                "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
                "CLANG_CXX_LIBRARY": "libc++",
                "MACOSX_DEPLOYMENT_TARGET": "10.7"
            },
            "msvs_settings": {
                "VCCLCompilerTool": {
                    "ExceptionHandling": 1
                }
            }
        },
        {
            "target_name": "stormlib-native",
            "sources": [
                "src/native/node-stormlib/main.cc"
            ],
            "include_dirs": [
                "<!@(node -p \"require(\\\"node-addon-api\\\").include\")"
            ],
            "dependencies": [
                "<!(node -p \"require(\\\"node-addon-api\\\").gyp\")",
                "deps-stormlib"
            ],
            "cflags!": [
                "-fno-exceptions"
            ],
            "cflags_cc!": [
                "-fno-exceptions"
            ],
            "xcode_settings": {
                "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
                "CLANG_CXX_LIBRARY": "libc++",
                "MACOSX_DEPLOYMENT_TARGET": "10.7"
            },
            "msvs_settings": {
                "VCCLCompilerTool": {
                    "ExceptionHandling": 1
                }
            }
        },
        {
            "target_name": "deps-casclib",
            "type": "static_library",
            "include_dirs": [
                "src/native/third-party/CascLib/src/"
            ],
            "sources": [
                "src/native/third-party/CascLib/src/common/Common.cpp",
                "src/native/third-party/CascLib/src/common/Directory.cpp",
                "src/native/third-party/CascLib/src/common/Csv.cpp",
                "src/native/third-party/CascLib/src/common/FileStream.cpp",
                "src/native/third-party/CascLib/src/common/FileTree.cpp",
                "src/native/third-party/CascLib/src/common/ListFile.cpp",
                "src/native/third-party/CascLib/src/common/Mime.cpp",
                "src/native/third-party/CascLib/src/common/RootHandler.cpp",
                "src/native/third-party/CascLib/src/common/Sockets.cpp",
                "src/native/third-party/CascLib/src/hashes/md5.cpp",
                "src/native/third-party/CascLib/src/hashes/sha1.cpp",
                "src/native/third-party/CascLib/src/jenkins/lookup3.c",
                "src/native/third-party/CascLib/src/overwatch/apm.cpp",
                "src/native/third-party/CascLib/src/overwatch/cmf.cpp",
                "src/native/third-party/CascLib/src/overwatch/aes.cpp",
                "src/native/third-party/CascLib/src/CascDecompress.cpp",
                "src/native/third-party/CascLib/src/CascDecrypt.cpp",
                "src/native/third-party/CascLib/src/CascDumpData.cpp",
                "src/native/third-party/CascLib/src/CascFiles.cpp",
                "src/native/third-party/CascLib/src/CascFindFile.cpp",
                "src/native/third-party/CascLib/src/CascIndexFiles.cpp",
                "src/native/third-party/CascLib/src/CascOpenFile.cpp",
                "src/native/third-party/CascLib/src/CascOpenStorage.cpp",
                "src/native/third-party/CascLib/src/CascReadFile.cpp",
                "src/native/third-party/CascLib/src/CascRootFile_Diablo3.cpp",
                "src/native/third-party/CascLib/src/CascRootFile_Install.cpp",
                "src/native/third-party/CascLib/src/CascRootFile_MNDX.cpp",
                "src/native/third-party/CascLib/src/CascRootFile_Text.cpp",
                "src/native/third-party/CascLib/src/CascRootFile_TVFS.cpp",
                "src/native/third-party/CascLib/src/CascRootFile_OW.cpp",
                "src/native/third-party/CascLib/src/CascRootFile_WoW.cpp",
                "src/native/third-party/CascLib/src/zlib/adler32.c",
                "src/native/third-party/CascLib/src/zlib/crc32.c",
                "src/native/third-party/CascLib/src/zlib/inffast.c",
                "src/native/third-party/CascLib/src/zlib/inflate.c",
                "src/native/third-party/CascLib/src/zlib/inftrees.c",
                "src/native/third-party/CascLib/src/zlib/zutil.c"
            ],
            "direct_dependent_settings": {
                "include_dirs": [
                    "src/native/third-party/CascLib/src"
                ]
            }
        },
        {
            "target_name": "deps-stormlib",
            "type": "static_library",
            "include_dirs": [
                "src/native/third-party/StormLib/src/"
            ],
            "sources": [
                "src/native/third-party/StormLib/src/adpcm/adpcm.cpp",
                "src/native/third-party/StormLib/src/huffman/huff.cpp",
                "src/native/third-party/StormLib/src/jenkins/lookup3.c",
                "src/native/third-party/StormLib/src/lzma/C/LzFind.c",
                "src/native/third-party/StormLib/src/lzma/C/LzmaDec.c",
                "src/native/third-party/StormLib/src/lzma/C/LzmaEnc.c",
                "src/native/third-party/StormLib/src/pklib/explode.c",
                "src/native/third-party/StormLib/src/pklib/implode.c",
                "src/native/third-party/StormLib/src/sparse/sparse.cpp",
                "src/native/third-party/StormLib/src/FileStream.cpp",
                "src/native/third-party/StormLib/src/SBaseCommon.cpp",
                "src/native/third-party/StormLib/src/SBaseDumpData.cpp",
                "src/native/third-party/StormLib/src/SBaseFileTable.cpp",
                "src/native/third-party/StormLib/src/SBaseSubTypes.cpp",
                "src/native/third-party/StormLib/src/SCompression.cpp",
                "src/native/third-party/StormLib/src/SFileAddFile.cpp",
                "src/native/third-party/StormLib/src/SFileAttributes.cpp",
                "src/native/third-party/StormLib/src/SFileCompactArchive.cpp",
                "src/native/third-party/StormLib/src/SFileCreateArchive.cpp",
                "src/native/third-party/StormLib/src/SFileExtractFile.cpp",
                "src/native/third-party/StormLib/src/SFileFindFile.cpp",
                "src/native/third-party/StormLib/src/SFileGetFileInfo.cpp",
                "src/native/third-party/StormLib/src/SFileListFile.cpp",
                "src/native/third-party/StormLib/src/SFileOpenArchive.cpp",
                "src/native/third-party/StormLib/src/SFileOpenFileEx.cpp",
                "src/native/third-party/StormLib/src/SFilePatchArchives.cpp",
                "src/native/third-party/StormLib/src/SFileReadFile.cpp",
                "src/native/third-party/StormLib/src/SFileVerify.cpp",
                "src/native/third-party/StormLib/src/SMemUtf8.cpp",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/rsa/rsa_verify_simple.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/misc/crypt_libc.c",
                
                "src/native/third-party/StormLib/src/libtomcrypt/src/hashes/hash_memory.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/hashes/md5.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/hashes/sha1.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/hashes/sha256.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/math/ltm_desc.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/math/multi.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/math/rand_prime.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/misc/base64_decode.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/misc/crypt_argchk.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/misc/crypt_find_hash.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/misc/crypt_find_prng.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/misc/crypt_hash_descriptor.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/misc/crypt_hash_is_valid.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/misc/crypt_ltc_mp_descriptor.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/misc/crypt_prng_descriptor.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/misc/crypt_prng_is_valid.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/misc/crypt_register_hash.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/misc/crypt_register_prng.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/misc/zeromem.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_decode_bit_string.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_decode_boolean.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_decode_choice.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_decode_ia5_string.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_decode_integer.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_decode_object_identifier.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_decode_octet_string.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_decode_printable_string.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_decode_sequence_ex.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_decode_sequence_flexi.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_decode_sequence_multi.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_decode_short_integer.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_decode_utctime.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_decode_utf8_string.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_encode_bit_string.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_encode_boolean.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_encode_ia5_string.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_encode_integer.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_encode_object_identifier.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_encode_octet_string.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_encode_printable_string.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_encode_sequence_ex.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_encode_sequence_multi.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_encode_set.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_encode_setof.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_encode_short_integer.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_encode_utctime.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_encode_utf8_string.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_length_bit_string.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_length_boolean.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_length_ia5_string.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_length_integer.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_length_object_identifier.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_length_octet_string.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_length_printable_string.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_length_sequence.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_length_utctime.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_sequence_free.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_length_utf8_string.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/asn1/der_length_short_integer.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/ecc/ltc_ecc_map.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/ecc/ltc_ecc_mul2add.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/ecc/ltc_ecc_mulmod.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/ecc/ltc_ecc_points.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/ecc/ltc_ecc_projective_add_point.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/ecc/ltc_ecc_projective_dbl_point.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/pkcs1/pkcs_1_mgf1.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/pkcs1/pkcs_1_oaep_decode.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/pkcs1/pkcs_1_pss_decode.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/pkcs1/pkcs_1_pss_encode.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/pkcs1/pkcs_1_v1_5_decode.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/pkcs1/pkcs_1_v1_5_encode.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/rsa/rsa_exptmod.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/rsa/rsa_free.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/rsa/rsa_import.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/rsa/rsa_make_key.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/rsa/rsa_sign_hash.c",
                "src/native/third-party/StormLib/src/libtomcrypt/src/pk/rsa/rsa_verify_hash.c"
            ],
            "direct_dependent_settings": {
                "include_dirs": [
                    "src/native/third-party/StormLib/src"
                ]
            },
            "defines": [
                "_7ZIP_ST",
                "BZ_STRICT_ANSI"
            ]
        }
    ]
}