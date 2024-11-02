#include <napi.h>

Napi::String Method(const Napi::CallbackInfo& info) {
  Napi::Env env = info.Env();
  return Napi::String::New(env, "I am STORMLIB!!");
}

Napi::Object Init(Napi::Env env, Napi::Object exports) {
  exports.Set(Napi::String::New(env, "stormlib"),
              Napi::Function::New(env, Method));
  return exports;
}

NODE_API_MODULE(stormlib, Init)