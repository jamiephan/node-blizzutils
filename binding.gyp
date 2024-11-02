{
    "targets": [
        {
            "target_name": "deps-casclib",
            "sources": [
                "src/node-casclib/main.cc"
            ],
            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include\")"
            ],
            "defines": [
                "NAPI_DISABLE_CPP_EXCEPTIONS"
            ]
        },
        {
            "target_name": "deps-stormlib",
            "sources": [
                "src/node-stormlib/main.cc"
            ],
            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include\")"
            ],
            "defines": [
                "NAPI_DISABLE_CPP_EXCEPTIONS"
            ]
        }
    ]
}