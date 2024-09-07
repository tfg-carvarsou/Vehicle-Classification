/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { VDImage } from '../models/VDImage'
import type { VDImagePostRequest } from '../models/VDImagePostRequest'
import type { CancelablePromise } from '../core/CancelablePromise'
import { OpenAPI } from '../core/OpenAPI'
import { request as __request } from '../core/request'
export class DetectorService {
  /**
   * Retrieve an image by its code
   * @param code
   * @returns VDImage The image has been retrieved successfully
   * @throws ApiError
   */
  public static detectorSnapviewRetrieve(code: string): CancelablePromise<VDImage> {
    return __request(OpenAPI, {
      method: 'GET',
      url: '/detector/snapview/{code}/',
      path: {
        code: code
      },
      errors: {
        400: `There has been an incident when retrieving the image. Please try again`,
        404: `The image does not exist`
      }
    })
  }
  /**
   * Delete an image by its code
   * @param code
   * @returns void
   * @throws ApiError
   */
  public static detectorSnapviewDestroy(code: string): CancelablePromise<void> {
    return __request(OpenAPI, {
      method: 'DELETE',
      url: '/detector/snapview/{code}/',
      path: {
        code: code
      },
      errors: {
        400: `There has been an incident when deleting the image. Please try again`,
        404: `The image does not exist`
      }
    })
  }
  /**
   * List all images
   * @returns VDImage The images has been listed successfully
   * @throws ApiError
   */
  public static detectorSnapzoneList(): CancelablePromise<Array<VDImage>> {
    return __request(OpenAPI, {
      method: 'GET',
      url: '/detector/snapzone/',
      errors: {
        400: `There has been an incident when listing the images. Please try again`
      }
    })
  }
  /**
   * Upload an image to detect vehicles
   * @param formData
   * @returns VDImage The image has been uploaded successfully
   * @throws ApiError
   */
  public static detectorSnapzoneCreate(formData: VDImagePostRequest): CancelablePromise<VDImage> {
    return __request(OpenAPI, {
      method: 'POST',
      url: '/detector/snapzone/',
      formData: formData,
      mediaType: 'multipart/form-data',
      errors: {
        400: `There has been an incident when uploading the image. Please try again`
      }
    })
  }
}
