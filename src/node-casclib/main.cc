#include <napi.h>

Napi::String Method(const Napi::CallbackInfo& info) {
  Napi::Env env = info.Env();
  return Napi::String::New(env, "I am CASCLIB!!");
}

Napi::Object Init(Napi::Env env, Napi::Object exports) {
  exports.Set(Napi::String::New(env, "casclib"),
              Napi::Function::New(env, Method));
  return exports;
}

NODE_API_MODULE(casclib, Init)