#include <napi.h>
#include "CascLib.h"

// Mapping For http://www.zezula.net/en/casc/casclib.html

// Accessing CASC storages
// =-=-=-=-=-=-=-=-=-=-=-=-=
// CascOpenStorageEx        	Opens a CASC storage
#include "./bindings/BCascOpenStorageEx.h"
// CascOpenStorage        	  Opens a local CASC storage
// CascOpenOnlineStorage      Opens an online CASC storage
// CascGetStorageInfo         Allows to retrieve an information about an open storage
// CascAddEncryptionKey       Allows to add an external encryption key
// CascFindEncryptionKey      Allows to find an encryption key
// CascCloseStorage         	Closes a CASC storage

// Reading files from a storage
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// CascOpenFile	              Opens a file from a storage
// CascGetFileSize 	          Retrieves a size of the file within storage
// CascGetFileSize64          Retrieves a size of the file within storage
// CascSetFilePointer       	Sets a new position within a file
// CascSetFilePointer64       Sets a new position within a file
// CascReadFile	              Reads data from the file
// CascGetFileInfo	          Retrieves an information about an open file within storage
// CascCloseFile	            Closes an open file

// File searching
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// CascFindFirstFile	        Finds a first file matching the specification
// CascFindNextFile	          Finds a next file matching the specification
// CascFindClose	            Stops searching in MPQ

Napi::String TestGreet(const Napi::CallbackInfo &info)
{
  Napi::Env env = info.Env();
  return Napi::String::New(env, "I am CASCLIB!!");
}

Napi::Object Init(Napi::Env env, Napi::Object exports)
{
  exports.Set(Napi::String::New(env, "_test_greet"),
              Napi::Function::New(env, TestGreet));

  exports.Set(Napi::String::New(env, "CascOpenStorageEx"),
              Napi::Function::New(env, BCascOpenStorageEx));
  return exports;
}

NODE_API_MODULE(casclib, Init)