#include <napi.h>
#include "StormLib.h"
#include "StormCommon.h"

Napi::String Method(const Napi::CallbackInfo &info)
{
  Napi::Env env = info.Env();
  return Napi::String::New(env, "I am stormlib!!");
}

Napi::Number Method2(const Napi::CallbackInfo &info)
{
  Napi::Env env = info.Env();
  HANDLE a = NULL;
  DWORD fileCount = 0;

  DWORD dwErrCode = ERROR_SUCCESS;

  if (!SFileOpenArchive("/workspaces/node-blizzutils/test/a.SC2Map", 0, STREAM_PROVIDER_FLAT, &a))
  {
    throw std::invalid_argument("received negative value");
  }
  SFileGetFileInfo(a, SFileMpqNumberOfFiles, &a, sizeof(fileCount), NULL);
  SFileCloseArchive(a);

  return Napi::Number::New(env, fileCount);
}

Napi::Object Init(Napi::Env env, Napi::Object exports)
{

  exports.Set(Napi::String::New(env, "stormlib"),
              Napi::Function::New(env, Method));

  exports.Set(Napi::String::New(env, "stormlib2"),
              Napi::Function::New(env, Method2));
  return exports;
}

NODE_API_MODULE(stormlib, Init)